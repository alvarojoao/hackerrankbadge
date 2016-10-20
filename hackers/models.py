# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import post_save, post_delete, pre_save

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models import Q
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

