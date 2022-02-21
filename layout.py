from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

def kpi(kpi_id,value,title):
    return html.Div(id=kpi_id+'-container', className = 'kpi-container',children = [
        html.Div(value, id = kpi_id, className = 'kpi-value-container'),
        html.Div(title, className = 'kpi-title-container')
    ])


layout = html.Div(className = 'html',children = [
    html.Div(id = 'toolbar', className = 'toolbar', children = [
        html.Div(id = 'info-flex-bar', className = 'info-flex-bar', children = [
            dbc.RadioItems(
            id="radios",
            className="btn-group",
            inputClassName="btn-check",
            labelClassName="btn btn-outline-primary",
            labelCheckedClassName="active",
            options=[
                {"label": "סך הכל", "value": 3},
                {"label": "עזה", "value": 2},
                {"label": 'איו"ש', "value": 1},
            ],
            value=3,
        )
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
        html.Div(id = 'registered-graph-container', className = 'graph-container', children = [
            dcc.Graph(id='registered-graph', className='graph')
        ]),
        html.Div(id = 'permits-graph-container', className = 'graph-container', children = [
            dcc.Graph(id='permits-graph', className='graph')
        ]),
        html.Div(id = 'passages-graph-container', className = 'graph-container', children = [
            dcc.Graph(id='passages-graph', className='graph')
        ]),
        html.Div(id = 'illegal-stays-graph-container', className = 'graph-container', children = [
            dcc.Graph(id='illegal-stays-graph', className='graph')
        ])
    ])
])
