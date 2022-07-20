import dash
# import dash_core_components as dcc
#from dash import dcc as dashComp
#from dash import html
import dash_html_components as html
import dash_core_components as dashComp
import plotly.express as px
import pandas as pandas
from dash.dependencies import Input, Output

# dataFrame = pandas.read_csv('ai_module1.csv')
dataFrame = pandas.read_csv('anomaly_detector.csv')


# print(dataFrame)
# print(dataFrame.vacuna_nombre.unique())
# dataFrame.vacuna_nombre.unique()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.H1("Vacunados por covid"),
        html.Img(src="assets/vacuna.webp")
    ], className="banner"),

    html.Div([
        html.Div([
            html.P("Selecciona la dosis", className="fix_label", style={"color" : "black", "margin-top" : "2px"}),
            dashComp.RadioItems(id = 'dosis-radioItems',
                                labelStyle={"display": 'inline-block'},
                                options=[
                                    {'label': 'Primera dosis', 'value': 'primera dosis cantidad'},
                                    {'label': 'Segunda dosis', 'value': 'Segunda dosis cantidad'}
                                ], value='primera dosis cantidad',
                                style={'text-align': 'center' ,'color':'black'}, className="dcc_compon" ),

        ], className='create_container2 five columns', style={'margin-bottom': '20px'})
    ], className='row flex-display '),

    html.Div([
        html.Div([
            dashComp.Graph(id = 'my_graph', figure={})
        ], className='create-container2 eight colums'),

        html.Div([
            dashComp.Graph(id = 'pie-graph', figure={})
        ], className="create-container2 five colums")

    ], className="row flex-display "),



], id='mainContainer', style={'display': 'flex', 'flex-direction':'column'})

@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioItems', component_property='value')])

def update_graph(value):
    if value == 'primera dosis cantidad':
        figura = px.line(
            data_frame=dataFrame,
            x='publlication_date',
            y='cost',

        )
    else:
        figura = px.bar(
            data_frame=dataFrame,
            x='popularity',
            y='revenue',

        )
    return figura

# Segundo Callback
# @app.callback(
#     Output('pie-graph', component_property='figure'),
#     [Input('dosis-radioItems', component_property='value')])

# def update_graph_pie(value):
#     if value == 'primer_dosis_cantidad':
#         figuraPastel = px.pie(
#             data_frame=dataFrame,
#             names='jurisdiccion_nombre',
#             values='primer_dosis_cantidad'
#         )
#     else:
#         figuraPastel = px.pie(
#             data_frame=dataFrame,
#             names='jurisdiccion_nombre',
#             values='segunda_dosis_cantidad'
#         )
#     return figuraPastel








if __name__ == ('__main__'):
    app.run_server(debug=True)

#Cambiar puerto PORT=5050