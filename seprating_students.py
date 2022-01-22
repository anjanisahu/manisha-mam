import pandas as pd
import csv
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
data_file=pd.read_csv("data_story.csv")
savings=list(data_file)
savings.pop(0)
total_entry=len(savings)
people_given_reminder=0
for i in savings:
    print(i[3])
    if(int (i[3])==1):
        people_given_reminder=people_given_reminder+1
fig=go.Figure(go.Bar(x=["Reminded", "Not Reminded"], y=[people_given_reminder,(total_entry - people_given_reminder)]))
fig.show()      
       

