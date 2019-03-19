import unittest
import analysisTesting
import json

class TestAnalysis(unittest.TestCase):

	# def test_sentiment(self):
	# 	#Positive test
	# 	self.assertGreater(analysisTesting.getSentiment("I love this car, it is amazing."), 0)
	# 	#Negative test
	# 	self.assertLess(analysisTesting.getSentiment("I hate this car, it is tertible."), 0)
	# 	#Negation test
	# 	self.assertLess(analysisTesting.getSentiment("I do not like this car."), 0)
	# 	self.assertGreater(analysisTesting.getSentiment("Disliking cars is not really my thing."), 0)
	# 	#Sarcasm test
	# 	self.assertLess(analysisTesting.getSentiment("Great, this car breakdown is all I need."), 0)
	# 	#Inverted meaning test (Negative term used in a positive way)
	# 	self.assertGreater(analysisTesting.getSentiment("Oh wow, that film was wicked"), 0)
	# 	self.assertGreater(analysisTesting.getSentiment("Let's go to the park, it will be sick."), 0)

	# def test_tokenization(self):
	# 	self.assertEqual(analysisTesting.nltkTokenize("It's eight o'clock on Thursday morning"), ["It's", 'eight', "o'clock", 'on', 'Thursday', 'morning'])
	# 	self.assertEqual(analysisTesting.tweetTokenize("It's eight o'clock on Thursday morning"), ["It's", 'eight', "o'clock", 'on', 'Thursday', 'morning'])

	# 	self.assertEqual(analysisTesting.nltkTokenize("Haha :) I can't believe it!"), ['Haha', ':)', 'I', "can't", 'believe', 'it', '!'])
	# 	self.assertEqual(analysisTesting.tweetTokenize("Haha :) I can't believe it!"), ['Haha', ':)', 'I', "can't", 'believe', 'it', '!'])

	# 	self.assertEqual(analysisTesting.nltkTokenize("@john, my favoutite color is red... :D #amazing"), ['@john', ',', 'my', 'favoutite', 'color', 'is', 'red', '...', ':D', '#amazing'])
	# 	self.assertEqual(analysisTesting.tweetTokenize("@john, my favoutite color is red... :D #amazing"), ['@john', ',', 'my', 'favoutite', 'color', 'is', 'red', '...', ':D', '#amazing'])

	# def test_wordFreq(self):
	# 	self.assertEqual(analysisTesting.wordFrequency(['There', 'is', 'one', 'of', 'each', 'word']), {'There': 1, 'is': 1, 'one': 1, 'of': 1, 'each': 1, 'word': 1})
	# 	self.assertEqual(analysisTesting.wordFrequency(['one', 'two', 'two', 'three', 'three', 'three']), {'three': 3, 'two': 2, 'one': 1})
	# 	self.assertEqual(analysisTesting.wordFrequency(['I', 'love', 'counting', 'words', 'upon', 'words', ':)']), {'words': 2, 'I': 1, 'love': 1, 'counting': 1, 'upon': 1, ':)': 1})
	# 	self.assertEqual(analysisTesting.wordFrequency(['@john', '#python', 'is', 'great', '...', 'thanks', ',', 'python']), {"@john": 1, "#python": 1, "is": 1, "great": 1, "...": 1, "thanks": 1, ",": 1, "python": 1})
	# 	self.assertEqual(analysisTesting.wordFrequency(['alpha', 'Alpha', 'ALPHA', '1', '2', '12', '1.2']), {"alpha": 1, "Alpha": 1, "ALPHA": 1, "1": 1, "2": 1, "12": 1, "1.2": 1})
	
	# def test_tfidf(self):
	# 	self.assertEqual(analysisTesting.tfidf(["hello this is a test"]), '{"test":0.7071067812,"hello":0.7071067812}')

	def test_clean(self):
		self.assertEqual(analysisTesting.clean("@john This is a great test https://www.google.co.uk"), ['great test'])
		self.assertEqual(analysisTesting.clean("@smith #python is the BEST https://www.python.org/"), ['python best'])
		self.assertEqual(analysisTesting.clean("clean this #tweet Please, 😃😋"), ['clean tweet'])
		self.assertEqual(analysisTesting.clean("It's 9am, Time for work! :("), ["it's 9am time work :("])