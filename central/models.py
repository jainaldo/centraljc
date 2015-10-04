# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

TURNOS = (
    (u'MANHÃ', u'Manhã'),
    ('NOITE', 'Noite'),
)


class Sala(models.Model):
    nome = models.CharField("Nome da Sala", max_length=255)
    turno = models.CharField(choices=TURNOS, max_length=50)
    slug = models.SlugField(blank=True, max_length=255, editable=False)

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"

    def __unicode__(self):
        return "%s (%s)" % (self.nome, self.get_turno_display())

    def save(self, *args, **kwargs):
        self.slug = slugify(self)
        return super(Sala, self).save(*args, **kwargs)


class Ficha(models.Model):
    n_ficha = models.IntegerField("Número da Ficha")
    crianca = models.CharField("Nome da criança", max_length=255)
    responsavel = models.CharField("Nome do responsável", max_length=255)
    telefone = models.CharField(max_length=25)
    sala = models.ForeignKey('Sala')
    ativo = models.BooleanField(default=True)
    criado_em = models.DateField(auto_now_add=True, editable=False)
    slug = models.SlugField(blank=True, max_length=255, editable=False)

    class Meta:
        verbose_name = "Ficha"
        verbose_name_plural = "Fichas"

    def __unicode__(self):
        return "%s (%s)" % (self.crianca, self.n_ficha)

    def save(self, *args, **kwargs):
        self.slug = slugify(self)
        return super(Ficha, self).save(*args, **kwargs)

    def set_ativo(self):
        if self.ativo:
            self.ativo = False
        else:
            self.ativo = True
        self.save()
