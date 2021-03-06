import csv
import pandas as pd
import plotly.graph_objects as pg

df = pd.read_csv('data.csv')
data = df.groupby("level")['attempt'].mean()
print(data)

graph = pg.Figure(pg.Bar(x = data,y = ['Level 1','Level 2','Level 3','Level 4'],orientation = 'h'))
graph.show()