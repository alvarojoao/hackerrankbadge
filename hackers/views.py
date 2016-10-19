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
from django.template import Context, Template
from django.http import Http404
from datetime import datetime

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

HR_LANG={"c":'devicon-c-line',
"cpp":'devicon-cplusplus-line',
"cpp14":'devicon-cplusplus-line',
"c#":'devicon-csharp-line',
"csharp":'devicon-csharp-line',
"python":'devicon-python-plain',
"python3":'devicon-python-plain',
"java":'devicon-java-plain',
"java8":'devicon-java-plain',
"php":'devicon-php-plain',
"text":'devicon-atom-original colored',
"text_pseudo":'devicon-atom-original colored',
"fortran":'',
"perl":'',
"ruby":'devicon-ruby-plain',
"objectivec":'',
"haskell":'',
"clojure":'',
"scala":'',
"commonlisp(sbcl)":'',
"lua":'',
"erlang":'devicon-erlang-plain',
"javascript":'devicon-javascript-plain',
"go":'devicon-go-plain colored',
"brainf**k":'',
"groovy":'',
"ocaml":'',
"fsharp":'',
"pypy":'',
"pypy3":'',
"vb.net":'',
"lolcode":'',
"smalltalk":'',
"tcl":'',
"r":'',
"gnuoctave":'',
"cobol":'',
"racket":'',
"rust":'',
"swift":'',
"pascal":'',
"bash":'',
"d":'',
"elixir":'',
"ada":'',
"nim":'',
"julia":'',
"oracle":'devicon-oracle-original colored',
"microsoftsql":'',
"mysql":'devicon-mysql-plain-wordmark colored',
"db2":''}


def simple_badge(request):
	"""
	home page
	"""
	try:
		show_image = request.GET.get('show_image','True')  in ['true', 'True']
		show_username = request.GET.get('show_username','True') in ['true', 'True']
		show_level = request.GET.get('show_level','True') in ['true', 'True']
		show_medals = request.GET.get('show_medals','True') in ['true', 'True']
		show_medals_details = request.GET.get('show_medals_details','True') in ['true', 'True']
		show_languages = request.GET.get('show_languages','True') in ['true', 'True']
		show_submissions_title = request.GET.get('show_submissions_title','True') in ['true', 'True']
		show_language_title = request.GET.get('show_language_title','True') in ['true', 'True']
		show_events = request.GET.get('show_events','True') in ['true', 'True']
		show_followers = request.GET.get('show_followers','True') in ['true', 'True']
		show_badges = request.GET.get('show_badges','True') in ['true', 'True']
		show_bio = request.GET.get('show_bio','True') in ['true', 'True']
		show_website = request.GET.get('show_website','True') in ['true', 'True']
		show_last_submmissions = request.GET.get('show_last_submmissions','True') in ['true', 'True']

		if show_image or show_username or show_level or show_events or show_followers or show_bio or show_website:
			profile = profile_rest(request.GET.get('username','alvarojoao'))
		if show_medals:
			contest = contest_rest(request.GET.get('username','alvarojoao'))
		if show_badges:
			badges = badges_rest(request.GET.get('username','alvarojoao'))
		if show_languages:
			languages = languages_rest(request.GET.get('username','alvarojoao')) 
		if show_last_submmissions:
			submissions = submissions_rest(request.GET.get('username','alvarojoao')) 

	except:
		raise Http404("Sorry can't find this username:"+request.GET.get('username','alvarojoao'))

	return render(request, 'simple_badge.html',  locals(), content_type='text/html')

def badges_rest(username='alvarojoao'):
	"""
	home page
	"""
	link = HR_URLS['badges'].replace('_username_',username)
	data = requests.get(link).json()
	return data

def profile_rest(username='alvarojoao'):
	"""
	home page
	"""
	link = HR_URLS['profile'].replace('_username_',username)
	data = requests.get(link).json()
	return data

def languages_rest(username='alvarojoao',numbers=3,unique = False):
	"""
	home page
	"""
	link = HR_URLS['profile'].replace('_username_',username)
	data = requests.get(link).json()
	model = data.get("model",None) 
	languages = model.get("languages",[]) if model is not None else []
	languages = map(lambda (x,y):(x,int(y),HR_LANG.get(x,None)),languages)
	if unique:
		uniqLanguagesdict = {}
		uniqLanguages = []
		for lang in languages:
			if not uniqLanguagesdict.has_key(lang[2]):
				uniqLanguages.append(lang)
				uniqLanguagesdict[lang[2]] = True
		languages = uniqLanguages
	languages = sorted(languages, key=lambda tup: tup[1], reverse=True)[:numbers]
	return languages


def contest_rest(username='alvarojoao'):
	link = HR_URLS['scores_elo'].replace('_username_',username)
	data = {}
	data.update({'datacontests': requests.get(link).json()})
	totalmedals = {}
	for area in data['datacontests']:
		contest = area.get('contest',None)
		medals = contest.get('medals',None) if contest is not None else None
		if medals:
			for medal,count in medals.items():
				totalmedals[medal] = totalmedals.get(medal,0) + count
	data.update({'totalmedals': totalmedals})
	return data

def submissions_rest(username='alvarojoao',last_days=8):
	link = HR_URLS['submission_histories'].replace('_username_',username)
	data = requests.get(link).json()
	today = datetime.today()
	new_start = today + timedelta(days=-1*last_days) #day can be negative
	last_submissions = []
	for date,count in data.items():
		date_object = datetime.strptime(date, '%Y-%m-%d')
		if date_object>new_start:
			last_submissions.append((date_object.strftime('%a'),count))
	return last_submissions

def badges(request):
	"""
	home page
	"""
	data = badges_rest(request.GET.get('username','alvarojoao'))
	return render(request, 'badges.html',  locals(), content_type='text/html')

def profile(request):
	"""
	home page
	"""
	data = profile_rest(request.GET.get('username','alvarojoao'))
	return render(request, 'profile.html',  locals(), content_type='text/html')


def language(request):
	"""
	home page
	"""
	data = languages_rest(request.GET.get('username','alvarojoao'))
	return render(request, 'languages.html',  locals(), content_type='text/html')

def contest(request):
	"""
	home page
	"""
	data = contest_rest(request.GET.get('username','alvarojoao'))
	return render(request, 'contest.html',  locals(), content_type='text/html')

def submissions(request):
	"""
	home page
	"""
	data = submissions_rest(request.GET.get('username','alvarojoao'))
	return render(request, 'submission_histories.html',  locals(), content_type='text/html')