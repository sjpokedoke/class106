import pandas as pd
import plotly.express as px

df = pd.read_csv("data4.csv")
fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
fig.show()