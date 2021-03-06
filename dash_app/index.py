"""index.py
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app #, models, execute_db
from apps import home, livedata


app.layout = html.Div([   
    html.Div([
        html.Div([
            html.H3('Heading for Multi Page App')
        ]),         
        dcc.Link('Home', href='/', style={'paddingRight':'10px'}),
        dcc.Link('Stats', href='/stats', style={'paddingRight':'10px'}),
        dcc.Link('Live', href='/live', style={'paddingRight':'10px'}),
        dcc.Location(id='url', refresh=False)
    ], className='navbar navbar-dark sticky-top mt-5'),
    dbc.Container(id='main-content', children='Main', className='', fluid=True)
], className='')


@app.callback(Output('main-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home.layout
    elif pathname == '/stats':
        return html.H3('Comming soon')
    elif pathname == '/live':
        return livedata.layout
    else:
        return html.H3('Page not found 404')


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')