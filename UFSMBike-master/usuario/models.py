#coding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from bicicleta.models import Bicicleta
from django.contrib.auth.models import PermissionsMixin, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, matricula, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not matricula:
            raise ValueError('Users must have an email address')

        user = self.model(
            matricula=self.normalize_email(matricula),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricula, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(matricula,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    #username
    matricula = models.CharField(primary_key=True,max_length=20)
    #resto
    cpf = models.IntegerField(null=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    tel = models.IntegerField(null=True)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    bicicletaAlugada = models.ForeignKey(Bicicleta, null=True, blank=True)
    multaSaldo = models.FloatField(default=25)
    #admin
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'matricula'
    objects = MyUserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.nome

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin


