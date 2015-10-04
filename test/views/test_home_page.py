# -*- coding: utf-8 -*-
from django.test import TestCase
from should_dsl import should
from django.core.urlresolvers import reverse
from central.models import Sala
from model_mommy import mommy
from django.test import Client

client = Client()


class TestViewHomePage(TestCase):

    def setUp(self):
        self.sala_1 = mommy.make(Sala, nome='Sala 6 anos', turno="Manhã")
        self.sala_2 = mommy.make(Sala, nome='Sala 7 anos', turno="Manhã")

    def test_url_HomePageView_sucesso(self):
        response = client.get(reverse('home'))
        response.status_code | should | equal_to(200)

    def test_index_template(self):
        response = client.get(reverse('home'))
        response.template_name[0] | should | equal_to('index.html')

    def test_mostrar_lista_de_todas_as_salas(self):
        response = client.get(reverse('home'))
        list_salas = Sala.objects.all()
        list(response.context['list_salas']) \
                                    | should | equal_to(list(list_salas))
