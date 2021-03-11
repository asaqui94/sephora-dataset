import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


df_love = pd.read_csv("sum_love_df.csv")
wdf_love = pd.read_csv("sum_love_wdf.csv")
mgr_options = df_love["brand"].unique()

app = dash.Dash()

body = html.Div([
    html.H2("Customer Love"),
    html.Div(
        [
            dcc.Dropdown(
                id="brand",
                options=[{
                    'label': i,
                    'value': i
                } for i in mgr_options],
                value='All Brands'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
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

def Coolgraph():
    layout = html.Div([
    body
    ])
    return layout


app.layout = Coolgraph()

if __name__ == '__main__':
    app.run_server(debug=True)
