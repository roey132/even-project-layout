from re import X
from attr import asdict
from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import layout
import pandas as pd

app = Dash(__name__)
app.layout = layout.layout

color_palette = ['#004c6d','#005e81','#007195','#0084a8','#0098bb','#00adce','#00c2df','#00d7f0','#00edff'].reverse()

def figFontColor(fig):
    color = 'white'
    fig.update_layout(
    font_family="Segoe UI",
    font_color=color,
    title_font_family="Segoe UI",
    title_font_color=color,
    legend_title_font_color=color)

    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})

def figTrasparentBackground(fig):
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',})

#graph callbacks
@app.callback(
    Output(component_id='illegal-stays-graph',component_property='figure'),
    Input(component_id='radios',component_property='value')
)
def illegalStaysGraph(value):
    if value == 3:
        fig = 3
    elif value == 2:
        fig = 2
    else:
        fig = 1

    fig = px.bar(x=[1,2,3,4,5],y=[1,2,3,4,5], color_discrete_sequence = ['#00c2df'],title='שוהים בלתי חוקיים')
    figTrasparentBackground(fig)
    figFontColor(fig)

    return fig

@app.callback(
    Output(component_id='passages-graph',component_property='figure'),
    Input(component_id='radios',component_property='value')
)
def passagesGraph(value):
    if value == 3:
        fig = 3
    elif value == 2:
        fig = 2
    else:
        fig = 1

    fig = px.line(x=[1,2,3,4,5],y=[6,3,4,7,4], color_discrete_sequence = ['#00c2df'], title = 'מעברים')
    figTrasparentBackground(fig)
    figFontColor(fig)
    return fig

@app.callback(
    Output(component_id='permits-graph',component_property='figure'),
    Input(component_id='radios',component_property='value')
)
def permitsGraph(value):
    if value == 3:
        fig = 3
    elif value == 2:
        fig = 2
    else:
        fig = 1

    fig = px.bar(x=[1,2,3,4,5],y=[4,2,5,4,6], color_discrete_sequence = ['#00c2df'], title = 'היתרים פעילים')
    figTrasparentBackground(fig)
    figFontColor(fig)

    return fig

@app.callback(
    Output(component_id='registered-graph',component_property='figure'),
    Input(component_id='radios',component_property='value')
)
def registeredGraph(value):
    if value == 3:
        fig = 3
    elif value == 2:
        fig = 2
    else:
        fig = 1

    fig = px.line(x=[1,2,6,7,10],y=[1,2,3,4,5], color_discrete_sequence = ['#00c2df'], title = 'רשומים לאפליקציה')
    figTrasparentBackground(fig)
    figFontColor(fig)
    return fig

#style callbacks
@app.callback(
    Output(component_id='illegal-stays-graph-container', component_property='style'),
    Output(component_id='passages-graph-container', component_property='style'),
    Input(component_id='radios', component_property='value')
)
def toggleIllegalStaysContainer(value):
    print(f'radios value changed to {value}')
    if value == 1:
        return {'display':'none'},{'width':'97%'}
    else:
        return {},{}

@app.callback(
    Output(component_id='illegal-stays-kpi-container',component_property='style'),
    Input(component_id='radios', component_property='value')
)
def toggleIllegalStaysKpi(value):
    if value == 1:
        return {'display':'none'}
    else:
        return {}

# kpi callbacks
@app.callback(
    Output(component_id='app-kpi',component_property='children'),
    Input(component_id='radios',component_property='value')
)
def appKpi(value):
    if value == 1:
        return 6
    elif value == 2:
        return 9
    else:
        return 15

@app.callback(
    Output(component_id='active-permit-kpi',component_property='children'),
    Input(component_id='radios',component_property='value')
)
def activePermitsKpi(value):
    if value == 1:
        return 6
    elif value == 2:
        return 9
    else:
        return 15

@app.callback(
    Output(component_id='passages-kpi',component_property='children'),
    Input(component_id='radios',component_property='value')
)
def passagesKpi(value):
    if value == 1:
        return 6
    elif value == 2:
        return 9
    else:
        return 15

@app.callback(
    Output(component_id='shabac-inc-kpi',component_property='children'),
    Input(component_id='radios',component_property='value')
)
def shabacIncKpi(value):
    if value == 1:
        return 6
    elif value == 2:
        return 9
    else:
        return 15

@app.callback(
    Output(component_id='corona-sick-kpi',component_property='children'),
    Input(component_id='radios',component_property='value')
)
def coronaSickKpi(value):
    if value == 1:
        return 6
    elif value == 2:
        return 9
    else:
        return 15

@app.callback(
    Output(component_id='corona-vacc-kpi',component_property='children'),
    Input(component_id='radios',component_property='value')
)
def coronaVaccKpi(value):
    if value == 1:
        return 6
    elif value == 2:
        return 9
    else:
        return 15

@app.callback(
    Output(component_id='corona-inc-kpi',component_property='children'),
    Input(component_id='radios',component_property='value')
)
def coronaIncKpi(value):
    if value == 1:
        return 6
    elif value == 2:
        return 9
    else:
        return 15

@app.callback(
    Output(component_id='illegal-stays-kpi',component_property='children'),
    Input(component_id='radios',component_property='value')
)
def illegalStaysKpi(value):
    if value == 1:
        return 6
    elif value == 2:
        return 9
    else:
        return 15


if __name__ == '__main__':
    app.run_server(debug=False)
