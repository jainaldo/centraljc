# -*- coding: utf-8 -*-
from django.test import TestCase
from should_dsl import should
from central.models import Ficha, Sala
from model_mommy import mommy
from django.db.models import CharField, IntegerField, ForeignKey, \
    BooleanField, SlugField


class TestModelFicha(TestCase):

    def setUp(self):
        self.sala = mommy.make(Sala)
        self.ficha = mommy.make(Ficha,
                                crianca='lucas', n_ficha="123",
                                responsavel="pedro", telefone="(99)9999999",
                                sala=self.sala)

    def test_criation_ficha(self):
        self.ficha | should | be_instance_of(Ficha)

    def test_verify_fields(self):
        field_crianca = Ficha._meta.get_field('crianca')
        field_n_ficha = Ficha._meta.get_field('n_ficha')
        field_responsavel = Ficha._meta.get_field('responsavel')
        field_telefone = Ficha._meta.get_field('telefone')
        field_sala = Ficha._meta.get_field('sala')
        field_ativo = Ficha._meta.get_field('ativo')
        field_slug = Ficha._meta.get_field('slug')
        field_crianca | should | be_instance_of(CharField)
        field_n_ficha | should | be_instance_of(IntegerField)
        field_responsavel | should | be_instance_of(CharField)
        field_telefone | should | be_instance_of(CharField)
        field_sala | should | be_instance_of(ForeignKey)
        field_ativo | should | be_instance_of(BooleanField)
        field_slug | should | be_instance_of(SlugField)

    def test_verbose_name(self):
        Ficha._meta.verbose_name | should | equal_to("Ficha")
        Ficha._meta.verbose_name_plural | should | equal_to("Fichas")

    def test__unicode__(self):
        self.ficha.__unicode__() | should | equal_to("lucas (123)")

    def test_set_status(self):
        self.ficha.ativo | should | equal_to(True)
        self.ficha.set_ativo()
        self.ficha.ativo | should | equal_to(False)

    def test_create_slug_in_save(self):
        self.ficha.crianca = 'pedro'
        self.ficha.save()
        self.ficha.slug | should | equal_to('pedro-123')