# -*- coding: utf-8 -*-
from django.test import TestCase
from should_dsl import should
from central.models import Sala
from model_mommy import mommy
from django.db.models import CharField, SlugField


class TestModelSala(TestCase):

    def setUp(self):
        self.sala_6 = mommy.make(Sala, nome='Sala 6 anos', turno="Manhã")

    def test_criation_sala(self):
        self.sala_6 | should | be_instance_of(Sala)

    def test_verify_fields(self):
        field_nome = Sala._meta.get_field('nome')
        field_turno = Sala._meta.get_field('turno')
        field_slug = Sala._meta.get_field('slug')
        field_nome | should | be_instance_of(CharField)
        field_turno | should | be_instance_of(CharField)
        field_slug | should | be_instance_of(SlugField)

    def test_verbose_name(self):
        Sala._meta.verbose_name | should | equal_to("Sala")
        Sala._meta.verbose_name_plural | should | equal_to("Salas")

    def test__unicode__(self):
        self.sala_6.__unicode__() | should | equal_to(u"Sala 6 anos (Manhã)")

    def test_create_slug_in_save(self):
        self.sala_6.nome = "Sala 8 anos"
        self.sala_6.save()
        self.sala_6.slug | should | equal_to('sala-8-anos-manha')
