#!/usr/bin/env python
#@a_trendy_bot
from wordnik import *
from textblob import TextBlob
from twython import Twython, TwythonError
import os, time, requests

#twitter creds and setup
APP_KEY = os.getenv('APP_KEY')
APP_SECRET = os.getenv('APP_SECRET')
OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_TOKEN_SECRET = os.getenv('OAUTH_TOKEN_SECRET')

#wordnik setup
WORDNIK_URL = 'http://api.wordnik.com/v4'
WORDNIK_KEY= os.getenv('WORDNIK_KEY')

#create twitter and wordnik clients
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
wordnik = swagger.ApiClient(WORDNIK_KEY, WORDNIK_URL)

def get_random_words():
	random_noun = TextBlob(requests.get(WORDNIK_URL + '/words.json/randomWord?minCorpusCount=10000&minDictionaryCount=5&excludePartOfSpeech=proper-noun,proper-noun-plural,proper-noun-posessive,suffix,family-name,idiom,affix&hasDictionaryDef=true&includePartOfSpeech=noun&maxLength=22&api_key=' + WORDNIK_KEY).json()['word']).words[0].pluralize()
	random_verb = requests.get(WORDNIK_URL + '/words.json/randomWord?excludePartOfSpeech=adjective&hasDictionaryDef=true&includePartOfSpeech=verb-transitive&minCorpusCount=1000&maxLength=122&limit=3&api_key=' + WORDNIK_KEY).json()['word']
	return (random_verb, random_noun)

def make_tweet():
	first = get_random_words()
	second = get_random_words()
	return first[0] + ' ' + first[1] + ', ' + second[0] + ' ' + second[1] + '.'

def run():
	status = make_tweet()
	twitter.update_status(status=status)
	print status
	time.sleep(7200)

if __name__ == '__main__':
	while True:
		run()
