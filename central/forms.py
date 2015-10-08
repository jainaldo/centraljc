# -*- coding: utf-8 -*-
from .models import Ficha
from django import forms


class FichaCreateForm(forms.ModelForm):

    class Meta:
        model = Ficha
        fields = ['n_ficha', 'crianca', 'responsavel', 'telefone']
