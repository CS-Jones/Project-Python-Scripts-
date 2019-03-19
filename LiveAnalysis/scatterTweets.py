import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import json
plotly.tools.set_credentials_file(username='CallumJonesUni', api_key='MNHkSzd4itjwHjMObfbR')

# Create random data with numpy
import numpy as np

tweets = []
timetweets = []
datax = []
timex = []




for line in open('sampleTweetsTime.json'):
    tweets.append(json.loads(line)['sentiment'])

for line in open('sampleTweetsTime.json'):
    timetweets.append(json.loads(line)['time'])
	


	
#datax.extend(tweets)
timex.extend(timetweets)
    
	
print(timetweets)	

#trace = go.Scatter(
    #x = datax,
  #  y = timex,
   # mode = 'markers'
#)

#data = [trace]

# Plot and embed in ipython notebook!
#py.plot(data, filename='basic-scatter')
