import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import json
import datetime
from collections import defaultdict
plotly.tools.set_credentials_file(username='', api_key='')




positive = []
negative = []
textpositive = []
timepositive = []
textnegative = []
timenegative = [] 



for line in open('100tweets.json'):
	if json.loads(line)['sentiment'] > 0:
		positive.append(json.loads(line)['sentiment'])
		textpositive.append(json.loads(line)['text'])
		timepositive.append(json.loads(line)['time'])
	else:
		negative.append(json.loads(line)['sentiment'])
		textnegative.append(json.loads(line)['text'])
		timenegative.append(json.loads(line)['time'])
    
	



		
trace0 = go.Scatter(
    x = timepositive,
    y = positive,
    name = 'Positive',
	text = textpositive,
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
    x = timenegative,
    y = negative,
    name = 'Negative',
	text = textnegative,
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
plotly.offline.plot(fig, filename='colourscattertest.html')

		
