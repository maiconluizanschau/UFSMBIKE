#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from area.models import Area

class Bicicleta(models.Model):
	id = models.AutoField(primary_key=True)
	modelo = models.CharField(max_length=100)
	emAluguel = models.BooleanField(default=False)
	emManutencao = models.BooleanField(default=False)
	areaAtual = models.ForeignKey(Area,null=True,blank=True,verbose_name='área Atual')

	def __unicode__(self):
	    return u"{} ({})".format(self.translation, self.word.lang.abbr)	