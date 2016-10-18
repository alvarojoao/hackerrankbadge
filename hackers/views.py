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
import json
import ast
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
# https://www.hackerrank.com/rest/hackers/alvarojoao/badges

HR_URLS={
'contests':'https://www.hackerrank.com/rest/contests/master/notifications/summary',
'unread_threads':'https://www.hackerrank.com/rest/threads/unread_threads',
'profile':'https://www.hackerrank.com/rest/contests/master/hackers/_username_/profile',
'contest_participation':'https://www.hackerrank.com/rest/hackers/_username_/contest_participation?offset=0&limit=5',
'recent_challenges':'https://www.hackerrank.com/rest/hackers/_username_/recent_challenges?offset=0&limit=5',
'recent_discussions':'https://www.hackerrank.com/rest/hackers/_username_/recent_discussions?offset=0&limit=5',
'badges':'https://www.hackerrank.com/rest/hackers/_username_/badges',
'scores_elo':'https://www.hackerrank.com/rest/hackers/_username_/scores_elo',
'rating_histories_elo':'https://www.hackerrank.com/rest/hackers/_username_/rating_histories_elo',
'submission_histories':'https://www.hackerrank.com/rest/hackers/_username_/submission_histories'}


def badges(request):
	"""
	home page
	"""
	link = HR_URLS['badges'].replace('_username_',request.GET['username'])
	data = requests.get(link).json()
	return render(request, 'badges.html',  locals(), content_type='text/html')

def profile(request):
	"""
	home page
	"""
	link = HR_URLS['profile'].replace('_username_',request.GET['username'])
	data = requests.get(link).json()
	return render(request, 'profile.html',  locals(), content_type='text/html')

def contest(request):
	"""
	home page
	"""
	link = HR_URLS['scores_elo'].replace('_username_',request.GET['username'])
	data = requests.get(link).json()
	totalmedals = {}
	for area in data:
		contest = area.get('contest',None)
		medals = contest.get('medals',None) if contest is not None else None
		if medals:
			for medal,count in medals.items():
				totalmedals[medal] = totalmedals.get(medal,0) + count

	return render(request, 'contest.html',  locals(), content_type='text/html')

def submissions(request):
	"""
	home page
	"""
	link = HR_URLS['submission_histories'].replace('_username_',request.GET['username'])
	data = requests.get(link).json()
	return render(request, 'submission_histories.html',  locals(), content_type='text/html')