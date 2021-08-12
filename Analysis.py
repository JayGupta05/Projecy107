import csv
import pandas as pd
import plotly.graph_objects as pg
import plotly_express as px

df = pd.read_csv('data.csv')
data = df.groupby(["student_id","level"],as_index=False)['attempt'].mean()
print(data)

#graph = pg.Figure(pg.Bar(x = data,y = ['Level 1','Level 2','Level 3','Level 4'],orientation = 'h'))
#graph.show()

figure = px.scatter(data,x = "student_id", y = "level", size = 'attempt', color = 'attempt')
figure.show()