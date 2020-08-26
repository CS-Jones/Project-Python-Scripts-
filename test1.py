import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly


# Create random data with numpy
import numpy as np


# Create a trace
trace = go.Scatter(
     x =[-0.0478,-0.5574, -0.3182, 0.1531,0.0772,-0.8625,-0.872,0.4201,-0.91,-0.0644,0.4404,-0.6486,0.5574,-0.8807,-0.8475,0.4199,0.0516,-0.8074,-0.7626,-0.5267,-0.3182,0.2732,-0.2177,0.0772,-0.34,0.3182,-0.34,-0.5719,0.7037,-0.0258,-0.8225,-0.6124,0.4451,-0.4404,-0.6486,0.8172,-0.6696],
	y = [1,2,3,4.5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,15,16,2,12,18,20,13,12,14,15,16,17,18],
    mode = 'markers'
)

data = [trace]

#py.iplot(data, filename='basic-scatter')

plotly.offline.plot(trace, filename='name.html')