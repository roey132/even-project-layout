from dash import Dash, html, dcc, Output, Input
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px


app = Dash(__name__)

app.layout = html.Div([
    html.Div(id = 'toolbar', children = [
        html.Div(id = 'info-flex-bar', children = [
            html.Button(),
            html.Button(),
            html.Button()
        ]),
        html.Div(id = 'kpi-flex-bar', children = [
            html.Div(),
            html.Div(),
            html.Div(),
            html.Div(),
            html.Div(),
            html.Div(),
            html.Div(),
            html.Div()                                    
        ])
    ]),
    html.Div(id = 'body', children = [
        html.Div(id = 'registered-graph-container'),
        html.Div(id = 'permits-graph-container'),
        html.Div(id = 'passages-graph-container'),
        html.Div(id = 'illegal-stays-graph-container')
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
