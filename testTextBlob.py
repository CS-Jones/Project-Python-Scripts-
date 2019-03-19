from textblob import TextBlob
from textblob import Word

text = TextBlob("Textblob is amazingly simple to use. What great fun!")
print(text.sentiment)
tokens = text.words
print(tokens)

word = []
for words in tokens:
    if not any(words in s for s in word):
        word.append(words)
        wordPol = TextBlob(word[-1])
        print(wordPol + ":", tokens.count(words), "Polartiy:", wordPol.sentiment.polarity)

