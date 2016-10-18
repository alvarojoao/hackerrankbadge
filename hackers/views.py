from django.shortcuts import render
from hackers.models import Hacker
# Create your views here.
from django.core import serializers
import json
from django.http import HttpResponse
import math
from datetime import datetime, date,timedelta
from urlparse import urlparse, parse_qs
import time
from django.db import transaction
from bs4 import BeautifulSoup
import urllib2
import urllib
import requests

# https://www.hackerrank.com/rest/contests/master/notifications/summary?_=1476764851227
# https://www.hackerrank.com/rest/threads/unread_threads?_=1476764851230
# https://www.hackerrank.com/rest/contests/master/hackers/alvarojoao/profile?_=1476764851231
# https://www.hackerrank.com/rest/hackers/alvarojoao/contest_participation?offset=0&limit=5&_=1476764851232
# https://www.hackerrank.com/rest/hackers/alvarojoao/recent_challenges?offset=0&limit=5&_=1476764851233
# https://www.hackerrank.com/rest/hackers/alvarojoao/recent_discussions?offset=0&limit=5&_=1476764851234
# https://www.hackerrank.com/rest/hackers/alvarojoao/badges?_=1476764851235
# https://www.hackerrank.com/rest/hackers/alvarojoao/scores_elo?_=1476764851236
# https://www.hackerrank.com/rest/hackers/alvarojoao/rating_histories_elo?_=1476764851237
# https://www.hackerrank.com/rest/hackers/alvarojoao/submission_histories?_=1476764851238
# https://www.hackerrank.com/rest/hackers/alvarojoao/scores_elo?_=1476764851239
# https://www.hackerrank.com/rest/hackers/alvarojoao/rating_histories_elo?_=1476764851240


def home(request):
	"""
	home page
	"""
	link = "https://www.hackerrank.com/rest/hackers/alvarojoao/badges"
	# f = urllib.urlopen(link).read()
	# url = raw_input("www.hackerrank.com/alvarojoao")

	r  = requests.get(link)

	data = r.text

	# page = urllib2.urlopen('').read()
	# soup = BeautifulSoup(page)
	# print soup.body.prettify()
	return HttpResponse(data)