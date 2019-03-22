import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import json
plotly.tools.set_credentials_file(username='', api_key='')
import numpy as np

N = 10
random_y = np.random.randn(N)

tweets = []
datax = []

for line in open('sampleTweets.json'):
    tweets.append(json.loads(line)['sentiment'])
    
tweets.append(datax)


trace = go.Scatter(
    x = datax,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.plot(data, filename='basic-scatter')

