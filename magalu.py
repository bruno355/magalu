import chart_studio as py
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd
from datetime import datetime

df = pd.read_csv(url, sep=',')

trace = go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])

layout = go.Layout(
    xaxis = dict(
        rangeslider = dict(
            visible = False
        )
    )
)

data = [trace]

fig = go.Figure(data=data,layout=layout)
pio.show(fig, filename='analise_financeiro_magalu')
