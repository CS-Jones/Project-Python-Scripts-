from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from nltk.tokenize import TweetTokenizer
import nltk

import pandas as pd
import numpy as np
import string
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text

import re

my_stop_words = text.ENGLISH_STOP_WORDS.union(string.punctuation)
tknzr = TweetTokenizer()
analyzer = SentimentIntensityAnalyzer()

def getSentiment(sentence):
	sentiment = analyzer.polarity_scores(sentence)['compound']

	return sentiment

def nltkTokenize(string):

	return nltk.tokenize.word_tokenize(string)

def tweetTokenize(string):
	tknzr = TweetTokenizer()

	return tknzr.tokenize(string)

def wordFrequency(string):
	return nltk.FreqDist(string)

def tfidf(string):
	vectorizer = TfidfVectorizer(min_df=1, tokenizer=tknzr.tokenize, stop_words=my_stop_words)
	X = vectorizer.fit_transform(string)
	df= pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
	for index, row in df.iterrows():
		s = pd.Series(df.loc[index].sort_values(ascending=False))[:50]

	return s.to_json()

def clean(string):
	tweetByte = string.encode('ascii', 'ignore').lower()
	cleanTweet = tweetByte.decode('UTF-8')
	tweet = re.sub(r"http\S+", "", cleanTweet)
	tweet = re.sub(r"@(\S+)", "", tweet)
	tweet = re.sub(r"#", "", tweet)
	tk = tknzr.tokenize(tweet)

	fltCorpus = [word for word in tk if word not in my_stop_words]

	fltString = [" ".join(fltCorpus)]

	return fltString