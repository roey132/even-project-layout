from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px


app = Dash(__name__)

app.layout = html.Div(className = 'html',children = [
    html.Div(id = 'toolbar', className = 'toolbar', children = [
        html.Div(id = 'info-flex-bar', className = 'info-flex-bar', children = [
            html.Button('asd', className = 'page-button'),
            html.Button('asd', className = 'page-button'),
            html.Button('asd', className = 'page-button')
        ]),
        html.Div(id = 'kpi-flex-bar', className = 'kpi-flex-bar', children = [
            html.Div('asd'),
            html.Div('asd'),
            html.Div('asd'),
            html.Div('asd'),
            html.Div('asd'),
            html.Div('asd'),
            html.Div('asd'),
            html.Div('asd')                                    
        ])
    ]),
    html.Div(id = 'body', className = 'body', children = [
        html.Div('asd', id = 'registered-graph-container', className = 'graph-container'),
        html.Div('asd', id = 'permits-graph-container', className = 'graph-container'),
        html.Div('asd', id = 'passages-graph-container', className = 'graph-container'),
        html.Div('asd', id = 'illegal-stays-graph-container', className = 'graph-container')
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
