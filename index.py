import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import App
from homepage import Homepage
from coolgraph import Coolgraph

df_love = pd.read_csv("sum_love_df.csv")
wdf_love = pd.read_csv("sum_love_wdf.csv")
mgr_options = df_love["brand"].unique()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])

@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('brand', 'value')])
def update_graph(brand):
    if brand== "Drunk Elephant":
        df_love_plot = df_love.copy()
    else:
        df_love_plot = df_love[df_love['brand'] == brand]



    trace1 = go.Bar(x=df_love.brand, y=df_love.love, name='All')
    trace2 = go.Bar(x=wdf_love.brand, y=wdf_love.love, name='Women')

    return {
        'data': [trace1, trace2],
        'layout':
        go.Layout(
            title='Customer Love For {}'.format(brand),
            barmode='group')
    }

@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/data':
        return App()
    elif pathname == '/coolgraph':
        return Coolgraph()
    else:
        return Homepage()



if __name__ == '__main__':
    app.run_server(debug=False)
