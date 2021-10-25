import pandas as pd
import plotly.express as px

df = pd.read_csv("data3.csv")
fig = px.scatter(df, x="Size of TV", y="\tAverage time spent watching TV in a week (hours)")
fig.show()