import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import json
import plotly.offline as offline
plotly.tools.set_credentials_file(username='', api_key='')

# Create random data with numpy
import numpy as np

tweets = []
timetweets = []
datax = []
timex = []
texttweets =[]
text = []



for line in open('100tweets.json'):
    tweets.append(json.loads(line)['sentiment'])

for line in open('100tweets.json'):
    timetweets.append(json.loads(line)['time'])
	
for line in open('100tweets.json'):
    texttweets.append(json.loads(line)['text'])

	
datax.extend(tweets)
timex.extend(timetweets)
text.extend(texttweets)


	
print(datax)	

trace = go.Scatter(
    x = datax,
    y = timex,
	mode='markers',
    text= text
)

layout = go.Layout(
    title='Sentiment and time',
	hovermode='closest'
)



fig = go.Figure(data=[trace], layout=layout)
# Plot and embed in ipython notebook!
#py.plot(data, filename='basic-scatter')

plotly.offline.plot(fig, filename='test.html')