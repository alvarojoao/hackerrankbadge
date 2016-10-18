from django.shortcuts import render
from abastecimento.models import Hacker
# Create your views here.
from django.core import serializers
import json
from django.http import HttpResponse
import math
from datetime import datetime, date,timedelta
from urlparse import urlparse, parse_qs
import time
from django.db import transaction


def home(request):
	"""
	home page
	"""
