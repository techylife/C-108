import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("C-108_project.csv")
fig = ff.create_distplot([df['Avg Rating']], ["Avg Rating"], show_hist=False)
fig.show()