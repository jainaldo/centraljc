# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic import View
from .models import Sala, Ficha
from datetime import date
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['list_salas'] = Sala.objects.all()
        return context


class SalaDetailView(DetailView, View):
    model = Sala

    def get_context_data(self, **kwargs):
        hoje = date.today()
        context = super(SalaDetailView, self).get_context_data(**kwargs)
        context['list_fichas'] =\
            Ficha.objects.filter(sala__slug=self.object.slug,
                                 criado_em=hoje
                                 )
        return context

    def post(self, request, *args, **kwargs):
        ficha = Ficha.objects.get(id=request.POST['ficha_id'])
        ficha.set_ativo()
        return HttpResponseRedirect(reverse('sala_detail',
                                    kwargs={'slug': self.get_object().slug}))
