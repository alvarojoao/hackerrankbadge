#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export import resources
from django.contrib.auth.admin import UserAdmin

from import_export.admin import ImportExportMixin, ImportExportModelAdmin
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User

# Register your models here.
from django.db import transaction
from abastecimento.models import Hacker
from django import forms
from django.utils.translation import ugettext_lazy as _

# class ResponsavelAdmin(UserAdmin):

# 	search_fields = ['username']

# admin.site.register(Responsavel, ResponsavelAdmin)


class HackerAdmin(admin.ModelAdmin):

	search_fields = ['username']


admin.site.register(Hacker, HackerAdmin)
