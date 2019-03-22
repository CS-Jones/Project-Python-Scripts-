import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import json
from collections import defaultdict
plotly.tools.set_credentials_file(username='', api_key='')



tweets = []
datax = []
dataneg = []
positive = []
negative = []
textpositive = []
textnegative = []
texttweets =[]
text = []

for line in open('sampleTweets.json'):
    tweets.append(json.loads(line)['sentiment'])
	
for line in open('sampleTweetsTime.json'):
    texttweets.append(json.loads(line)['text'])

    
	
datax.extend(tweets)
text.extend(texttweets)
	

for num in tweets: 
	if (num > 0):		
		positive.append(num)
	else:
		negative.append(num)



		
		
		
trace0 = go.Scatter(
    x = [1,2,3,4.5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,15,16,2,12,18,20,13,12,14,15,16,17,18],
    y = positive,
    name = 'Positive',
	text = text,
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(152, 0, 0, .8)',
        line = dict(
            width = 2,
            color = 'rgb(0, 0, 0)'
        )
    )
)
    
trace1 = go.Scatter(
    x = [1,2,3,4.5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,15,16,2,12,18,20,13,12,14,15,16,17,18],
    y = negative,
    name = 'Negative',
	text = text,
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(255, 182, 193, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = 'Positive and Negative Sentiment across a day.',
              yaxis = dict(zeroline = False),
              xaxis = dict(zeroline = False),
			  hovermode='closest'
             )

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='test.html')

		
