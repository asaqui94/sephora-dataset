import pandas as pd
import pickle

import cufflinks as cf
cf.go_offline()
from chart_studio.plotly import plot, iplot
from plotly.offline import iplot

import plotly.graph_objects as go
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

from navbar import Navbar

df1 = pd.read_csv("avg_rating_df1.csv")
women_df1 = pd.read_csv("avg_rating_wdf1.csv")

df_love=pd.read_csv("sum_love_df.csv")
wdf_love=pd.read_csv("sum_love_wdf.csv")

nav = Navbar()
body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     dcc.Graph(
                         id='box_graph',
                         figure={
                             'data': [
                                 {'x':df_love['brand'][80:200:20], 'y':df_love['love'], 'type': 'bar', 'name': 'All Brands'},
                                 {'x':wdf_love['brand'], 'y':wdf_love['love'], 'type': 'bar', 'name': 'Women Brands'},
                                 
                             ],
                             'layout': {
                                 'title': 'Customer Love'
                             }
                             
                         }
                     )
                           
                   ],
                  md=4,
               ),
              dbc.Col(
                 [
                     dcc.Graph(
                         id='box_graph',
                         figure={
                             'data': [
                                 {'x':df1['brand'][0:100:20], 'y':df1['rating'], 'type': 'bar', 'name': 'All Brands'},
                                 {'x':women_df1['brand'], 'y':women_df1['rating'], 'type': 'bar', 'name': 'Women Brands'},
                             ],
                             'layout': {
                                 'title': 'Customer Rating'
                             }
                             
                         }
                     )



        

                        ]
                     ),
                ]
            )
       ],
className="mt-4",
)


def App():
    layout = html.Div([
        nav,
        body
    ])
    return layout