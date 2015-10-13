# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from .models import Sala, Ficha
from datetime import date
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import FichaCreateForm
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.template import RequestContext
from django.shortcuts import render_to_response


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['list_salas'] = Sala.objects.all()
        return context


class SalaDetailView(FormMixin, DetailView):
    model = Sala
    form_class = FichaCreateForm

    def get_success_url(self):
        self.object = self.get_object()
        return reverse('sala_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        hoje = date.today()
        context = super(SalaDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['list_fichas'] = Ficha.objects.filter(
            sala__slug=self.object.slug,
            criado_em=hoje)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if '_submit_ficha_id_status' in self.request.POST:
            ficha = get_object_or_404(
                Ficha,
                id=request.POST['_submit_ficha_id_status'])
            ficha.set_ativo()
            return HttpResponseRedirect(
                reverse('sala_detail', kwargs={'slug': self.object.slug}))
        elif '_submit_ficha_form' in self.request.POST:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.sala = self.get_object()
        form.save()
        messages.add_message(
            self.request, messages.SUCCESS,
            'Cadastrado com sucesso!')
        return super(SalaDetailView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR,
            'Verifique os erros no formulário.')
        return super(SalaDetailView, self).form_invalid(form)


def ajax_ficha_search(request):
    context = RequestContext(request)
    hoje = date.today()
    if request.is_ajax():
        q = request.GET.get('q')
        sala_id = request.GET.get('sala_id')
        sala = get_object_or_404(
            Sala,
            id=sala_id)
        list_fichas = Ficha.objects.filter(
            sala=sala,
            criado_em=hoje)
        if q:
            list_fichas = list_fichas.filter(
                Q(n_ficha__contains=q) |
                Q(crianca__contains=q) |
                Q(responsavel__contains=q)).order_by('n_ficha')
        return render_to_response(
            'central/table_ficha.html',
            {'list_fichas': list_fichas},
            context)
