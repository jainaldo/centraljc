# -*- coding: utf-8 -*-
from django.test import TestCase
from should_dsl import should
from django.test import Client
from django.core.urlresolvers import reverse
from central.models import Sala, Ficha
from model_mommy import mommy

client = Client()


class TestViewSalaDetail(TestCase):

    def setUp(self):
        self.sala_1 = mommy.make(Sala, nome='Sala 6 anos', turno="Manhã")
        self.ficha_1 = mommy.make(Ficha, n_ficha=123, crianca=u"João",
                                  sala=self.sala_1)

    def test_url_SalaDetailView_sucesso(self):
        response = client.get(reverse('sala_detail',
                              kwargs={'slug': self.sala_1.slug}))
        response.status_code | should | equal_to(200)

    def test_url_SalaDetailView_erro(self):
        response = client.get(reverse('sala_detail',
                              kwargs={'slug': 'meu-slug'}))
        response.status_code | should | equal_to(404)

    def test_mostra_lista_fichas_da_sala_de_hoje(self):
        response = client.get(reverse('sala_detail',
                              kwargs={'slug': self.sala_1.slug}))
        response.context['list_fichas'][0] \
                                    | should | equal_to(self.ficha_1)

    def test_url_SalaDetailView_redirect_post(self):
        response = client.post(reverse('sala_detail',
                                       kwargs={'slug': self.sala_1.slug}),
                               {'ficha_id': self.ficha_1.id})
        response.status_code | should | equal_to(302)
