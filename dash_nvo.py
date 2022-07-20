import dash
# import dash_core_components as dcc
#from dash import dcc as dashComp
#from dash import html
import dash_html_components as html
import dash_core_components as dashComp
import plotly.express as px
import pandas as pandas
from dash.dependencies import Input, Output
from datetime import datetime   # para poder usar la fecha actual
import dateutil.parser


# dataFrame = pandas.read_csv('ai_module1.csv')
dataFrame = pandas.read_csv('anomaly_detector.csv')
# tmp = '2022-06-02 00:00:00.0000000'
# tmp2 = dateutil.parser.parse(tmp).date()
# print(tmp2)


# dataFrame['publication_date']
pandas.to_datetime(dataFrame['publication_date'])

# print(dataFrame.vacuna_nombre.unique())
# dataFrame.vacuna_nombre.unique()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div([
        html.H1("Prueba"),
        # html.Img(src="assets/vacuna.webp")
    ], className="banner"),

    html.Div([
        html.Div([
            html.P("Selecciona la dosis", className="fix_label",
                   style={"color": "black", "margin-top": "2px"}),
            dashComp.RadioItems(id='dosis-radioItems',
                                labelStyle={"display": 'inline-block'},
                                options=[
                                    {'label': 'Primera dosis',
                                        'value': 'primera dosis cantidad'},
                                    {'label': 'Segunda dosis',
                                        'value': 'Segunda dosis cantidad'}
                                ], value='primera dosis cantidad',
                                style={'text-align': 'center', 'color': 'black'}, className="dcc_compon"),

        ], className='create_container2 five columns', style={'margin-bottom': '20px'})
    ], className='row flex-display '),

    html.Div([
        html.Div([
            dashComp.Graph(id='my_graph', figure={})
        ], className='create-container2 eight colums'),

        html.Div([
            dashComp.Graph(id='pie-graph', figure={})
        ], className="create-container2 five colums")

    ], className="row flex-display "),

    html.Div([
        html.Div([
            dashComp.Graph(id='my_graph3', figure={})
        ], className='create-container2 eight colums'),

        html.Div([
            dashComp.Graph(id='my_graph4', figure={})
        ], className="create-container2 five colums")

    ], className="row flex-display "),



], id='mainContainer', style={'display': 'flex', 'flex-direction': 'column'})


@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioItems', component_property='value')]
    )
def update_graph(value):
    if value == 'primera dosis cantidad':
        figura = px.histogram(
            data_frame=dataFrame,
            x='cause',
            y='location_id',
            histfunc='count',
            color='cause',
            marginal='box',
            title='Histograma de cantidad de anomalias por causa',
            # color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
            color_discrete_sequence=['#F0EBE3', '#E4DCCF', '#7D9D9C', '#576F72', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta'],
            width=800,
            height=500,


        )
    # else:
    #     figura = px.bar(
    #         data_frame=dataFrame,
    #         x='popularity',
    #         y='revenue',

    #     )
    return figura

# Segundo Callback


@app.callback(
    Output('pie-graph', component_property='figure'),
    [Input('dosis-radioItems', component_property='value')]
    )
def update_graph_pie(value):
    if value == 'primera dosis cantidad':
        figuraPastel = px.pie(
            data_frame=dataFrame,
            names='cause',
            values='location_id',
            title='Cantidad de Anomalias por Causa',
            color_discrete_sequence=['#F0EBE3', '#E4DCCF', '#7D9D9C', '#576F72', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta'],
        )
    else:
        figuraPastel = px.pie(
            data_frame=dataFrame,
            names='cause',
            values='location_id',



        )
    return figuraPastel

#tercer Callback
@app.callback( # Callback que actualiza el grafico 3
    Output('my_graph3', component_property='figure'),
    [Input('dosis-radioItems', component_property='value')]
    )
def update_graph_3(value):
    if value == 'primera dosis cantidad':
        figura3 = px.histogram(
            data_frame=dataFrame,
            x='publication_date',
            y='location_id',
            histfunc='count',
            color='publication_date',
            marginal='box',
            title='Histograma de cantidad de anomalias por fecha',
            # color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
            color_discrete_sequence=['#F0EBE3', '#E4DCCF', '#7D9D9C', '#576F72', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta'],
            width=800,
            height=500,


        )
        
    else:
        figura3 = px.histogram(
            data_frame=dataFrame,
            x='publication_date',
            y='location_id',
            histfunc='count',
            color='publication_date',
            marginal='box',
            title='Histograma de cantidad de anomalias por fecha',
            # color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
            color_discrete_sequence=['#F0EBE3', '#E4DCCF', '#7D9D9C', '#576F72', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta'],
            width=800,
            height=500,


        )
    return figura3

#Cuarto Callback
@app.callback( # Callback que actualiza el grafico 4
    Output('my_graph4', component_property='figure'),
    [Input('dosis-radioItems', component_property='value')]
    )
def update_graph_4(value):
    if value == 'primera dosis cantidad':
        figura4 = px.scatter(
            data_frame=dataFrame,
            x='publication_date',
            y='cause',
            # names='cause',
            # values='location_id',
            # parents='cause',

            # histfunc='count',
            color='cause',
            # marginal='box',
            title='sunburst de cantidad de anomalias por fecha',
            color_discrete_sequence=['#F0EBE3', '#E4DCCF', '#7D9D9C', '#576F72', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta'],
            width=800,
            height=500,


        )
    
    else:
        figura4 = px.histogram(
            data_frame=dataFrame,
            x='publication_date',
            y='location_id',
            histfunc='count',
            color='publication_date',
            marginal='box',
            title='Histograma de cantidad de anomalias por fecha',
            # color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'],
            color_discrete_sequence=['#F0EBE3', '#E4DCCF', '#7D9D9C', '#576F72', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta'],
            width=800,
            height=500,


        )
    return figura4
    # else:
    #     figura = px.bar(
    #         data_frame=dataFrame,
    #         x='popularity',
    #         y='revenue',

    #     )
    return figura3

# tmp = '2022-06-02 00:00:00.0000000'
# tmp2 = dateutil.parser.parse(tmp).date()
# print(tmp2)


if __name__ == ('__main__'):
    app.run_server(debug=True)

# Cambiar puerto PORT=5050
