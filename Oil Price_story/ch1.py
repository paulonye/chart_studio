import numpy as np
import pandas as pd
import plotly.graph_objects as go
import chart_studio.plotly as py
import datetime as dt


rop = pd.read_csv('rop.csv')
rop = rop.dropna()
rop['Date'] = pd.to_datetime(rop['Date'])
new_v = {1:'Jan', 2:'Feb', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'Aug', 9:'Sep', 10:'Oct'}
rop['Monthno'] =rop['Date'].dt.month
rop['Day'] = rop['Date']. dt.day
rop['Month'] = rop['Monthno'].replace(new_v)
rop['Ndate'] = rop['Month']+'-'+rop['Day'].astype('str')
rop = rop.set_index(rop['Ndate'])

fig = go.Figure()

fig.add_traces(go.Scatter(
                x = rop['Ndate'].loc[:'March-6'],
                y = rop['Adj Close'].loc[:'March-6'],
                mode = 'lines+markers', name = 'Lockdown Begins',
                line = dict(width = 1, color = 'blue'),
                marker = dict(size = 4, color = 'white', line = dict(color = 'blue', width = 2))
                ))


fig.add_traces(go.Scatter(
                x = rop['Ndate'].loc['March-6':'April-8'],
                y = rop['Adj Close'].loc['March-6':'April-8'],
                mode = 'lines+markers', name = 'Saudi and Russia Price War',
                line = dict(width = 1, color = 'black'),
                hovertemplate = 'Oil price:$%{y}',
                marker = dict(size = 4, color = 'white', line = dict(color = 'black', width = 2))))

fig.add_traces(go.Scatter(
                x = rop['Ndate'].loc['April-9':'April-21'],
                y = rop['Adj Close'].loc['April-9':'April-21'],
                mode = 'lines+markers', name = 'Reports of Storage Issues',
                line = dict(width = 1, color = 'red'),
                hovertemplate = 'Oil price:$%{y}',
                marker = dict(size = 4, color = 'white', line = dict(color = 'red', width = 2))))

fig.add_traces(go.Scatter(
                x = rop['Ndate'].loc['April-21':'May-1'],
                y = rop['Adj Close'].loc['April-21':'May-1'],
                mode = 'lines+markers', name = 'Oil Price Recovey',
                line = dict(width = 1, color = 'yellow'),
                hovertemplate = 'Oil price:$%{y}',
                marker = dict(size = 4, color = 'white', line = dict(color = 'yellow', width = 2))))

fig.add_traces(go.Scatter(
                x = rop['Ndate'].loc['May-1':],
                y = rop['Adj Close'].loc['May-1':],
                mode = 'lines+markers', name = 'OPEC meeting',
                line = dict(width = 1, color = 'green'),
                hovertemplate = 'Oil price:$%{y}',
                marker = dict(size = 4, color = 'white', line = dict(color = 'green', width = 2))))


x_vals = ['Jan-2', 'Feb-3', 'March-2', 'April-1', 'May-1', 'June-1', 'July-1', 'Aug-2', 'Sep-1', 'Oct-1']
x_labs = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']
ann = dict(text = '<b>Source: YahooFinance.com', xref = 'paper', yref = 'paper', x = 1, y = 1.05, font = dict(size = 10), showarrow = False)
annt = []
annt.append(ann)
fig.update_layout(
                yaxis = dict(zeroline = True, zerolinecolor = 'red',showticklabels = False, mirror = 'allticks',
                            showline = False, linecolor = 'black', side = 'left', showgrid = True, nticks =7,
                            gridcolor = 'black', zerolinewidth = 2, tickmode = 'auto'
                            ),
                xaxis = dict(showgrid = False, tickangle = 0, ticks = 'outside', showline = True,
                            linecolor = 'black', mirror = True, tickmode = 'array', linewidth = 4,
                            tickvals = x_vals, ticktext = x_labs, range = (-5,len(rop)),
                            tickfont = dict(color = 'black')
                            ),
                plot_bgcolor = 'silver',
                paper_bgcolor = 'silver',
                hovermode = 'x unified', hoverlabel = dict(font_size = 15, bgcolor = 'crimson', font_color = 'white'), 
                height = 700, width = 1200,
                grid = dict(rows = 4),
                title = dict(text = '<b>WTI Oil Price', x = 0.06, y = 0.9, font = dict(size = 30)),
                annotations = annt
)

py.plot(fig, filename = 'Oilprice_Story')