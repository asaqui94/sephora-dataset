import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table

from navbar import Navbar
nav = Navbar()

df = pd.read_csv("sephora_website_dataset.csv")
women_df = pd.read_csv("women_owned_brands.csv")
body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H2("Do Women Do It Better?"),
                     html.P(
                         """\
Over the past decade a revolution has been unfolding in the business world. We have been seeing a shift in diversity in many corporations. I will specifically be focusing on the beauty industry with a dataset from the Sephora website as of April 2020 
to see if women owned brands perform better than their male counterparts. I will compare the top 6 of my favorite women owned brands- Anastasia Beverly Hills, Drunk Elephant, Drybar, Fenty Beauty, Laura Mercier, and Huda Beauty- to other beauty brands available in Sephora based on ratings
and customer feedback."""
                           ),
                           dbc.Button("View details", outline=True, color="info"),
                   ],
                  md=4,
               ),
              dbc.Col(
                 [
   
    html.Div(children=[
                     html.P(id = 'text-1',
                   children = 'All Sephora Brands'),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} 
                 for i in df.columns[1:9]],
        fixed_columns={ 'headers': True, 'data': 1},
        style_table={'minWidth': '100%'},
        fixed_rows={ 'headers': True, 'data': 0},
        data=df.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="paleturquoise"),
        style_data=dict(backgroundColor="lavender")
        
    ),

        ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),
    html.Div(children=[
                     html.P(id='text-2',
                   children='Top 6 Women Owned Brands'),
    dash_table.DataTable(
        id='table2',
        columns=[{"name": j, "id": j} 
                 for j in women_df.columns[1:9]],
        fixed_columns={ 'headers': True, 'data': 1},
        style_table={'minWidth': '100%'},
        fixed_rows={ 'headers': True, 'data': 0},
        data=women_df.to_dict('records'),
        style_cell=dict(textAlign='left'),
        style_header=dict(backgroundColor="pink"),
        style_data=dict(backgroundColor="lavender")
    ),            

        ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),

        

                        ]
                     ),
                ]
            )
       ],
className="mt-4",
)

def Homepage():
    layout = html.Div([
    nav,
    body
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.layout = Homepage()
if __name__ == "__main__":
    app.run_server()