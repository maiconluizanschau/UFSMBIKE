#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Area(models.Model):
    id = models.AutoField(primary_key=True)
    x = models.CharField(verbose_name='Coordenada X',max_length=10)
    y = models.CharField(verbose_name='Coordenada Y',max_length=10)
    nome = models.CharField(max_length=100)

    def __str__(self):
    	return self.nome

	def __unicode__(self):
	    return u"{} ({})".format(self.translation, self.word.lang.abbr)	
