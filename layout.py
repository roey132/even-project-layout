from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

def kpi(kpi_id,value,title):
    return html.Div(className = 'kpi-container',children = [
        html.Div(value, id = kpi_id, className = 'kpi-value-container'),
        html.Div(title, className = 'kpi-title-container')
    ])

app = Dash(__name__)

app.layout = html.Div(className = 'html',children = [
    html.Div(id = 'toolbar', className = 'toolbar', children = [
        html.Div(id = 'info-flex-bar', className = 'info-flex-bar', children = [
            html.Button('asd', className = 'page-button'),
            html.Button('asd', className = 'page-button'),
            html.Button('asd', className = 'page-button')
        ]),
        html.Div(id = 'kpi-flex-bar', className = 'kpi-flex-bar', children = [
            kpi('app-kpi','15','רשומים לאפליקציה'),
            kpi('active-permit-kpi','15','היתרים פעילים'), 
            kpi('passages-kpi','15','עברו היום במעברים'), 
            kpi('shabac-inc-kpi','15','אחוז שינוי מניעות שבכ'), 
            kpi('corona-sick-kpi','15','חולים בקורונה'), 
            kpi('corona-vacc-kpi','15','מחוסנים לקורונה'), 
            kpi('corona-inc-kpi','15','מניעות קורונה'), 
            kpi('illegal-stays-kpi','15','שבחים')                             
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
