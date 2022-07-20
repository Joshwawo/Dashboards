from turtle import color
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('covidVacunados.csv')

# print(df)
# print(df.vacuna_nombre.nunique())
# print(df.vacuna_nombre.unique())

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
        html.H1('Vacunados por covid'),

    ], className='banner'),

    html.Div([
        html.Div( [
            html.P('Selecciona la dosis', className='fix_label',
                   style={'color': 'black', 'margin-top': '2px'}),
            dcc.RadioItems(id='dosis-radioitems',
                           labelStyle={'display': 'inline-block',  },
                           options=[
                               {'label': 'Primera dosis',
                                   'value': 'primera_dosis_cantidad'},
                               {'label': 'Segunda dosis',
                                'value': 'segunda_dosis_cantidad'}
                           ], value='primera_dosis_cantidad',
                           style={'text-aling': 'center', 'color': 'black'}, className='dcc_compon'),
        ], className='create_container2 five columns', style={'margin': '0 auto', }),
    ], className='row flex-display ')  ,

    html.Div([
        html.Div([
            dcc.Graph(id='my_graph', figure={})
        ], className='create_container2 eight columns'),

        html.Div([
            dcc.Graph(id='pie_graph', figure={})
        ], className='create_container2 five columns')
    ], className='row flex-display'),

    html.Div([  # Div para el gráfico de barras
        html.Div([
             dcc.Graph(id='bar_graph', figure={})
             ], className='create_container2 eight columns'),

        html.Div([
            dcc.Graph(id='bar_graph2', figure={})
        ], className='create_container2 five columns')
    ], className='row flex-display'),
    html.Div([
        html.Div([
            dcc.Graph(id='other_graph', figure={})
        ], className='create_container2 eight columns'),

        html.Div([
            dcc.Graph(id='other_graph2', figure={})
        ], className='create_container2 five columns')
    ], className='row flex-display'),
    html.Div([
        # html.Div([
        #     dcc.Graph(id='other_graph3', figure={})
        # ], className='create_container2 eight columns'),

        # html.Div([
        #     dcc.Graph(id='other_graph4', figure={})
        # ], className='create_container2 five columns')
    ], className='row flex-display'),

], id='mainContainer', style={'display': 'flex', 'flex-direction': 'column', 'background-color': 'white'})


# Figura 1
@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])
def update_graph(value):

    if value == 'primera_dosis_cantidad':
        fig = px.scatter(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='primera_dosis_cantidad',
            color_discrete_map={'cantidad': '#E72B1C'},

            labels={'cantidad': 'Cantidad'},

            title='Vacunados por covid en primera dosis',




        )

        fig.update_layout(
            title='Vacunados por covid primera dosis',
            xaxis_title='Jurisdiccion',
            yaxis_title='Cantidad',

            font=dict(

                size=12,
                color='#7f7f7f'
            ))

        return fig
    else:
        fig = px.scatter(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='segunda_dosis_cantidad')
        fig.update_layout(
            title='Vacunados por covid en segunda dosis',
            xaxis_title='Jurisdiccion',
            yaxis_title='Cantidad',

            font=dict(

                size=12,
                color='#7f7f7f'
            ))

        return fig


# Figura 2 pie
@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])
def update_graph_pie(value):

    if value == 'primera_dosis_cantidad':
        fig2 = px.pie(
            data_frame=df,
            names='jurisdiccion_nombre',
            values='primera_dosis_cantidad',
            color='primera_dosis_cantidad',


        )

        fig2.update_layout(
            title='Vacunados por covid en primera dosis',
            font=dict(

                size=12,
                color='#7f7f7f'
            ))

        return fig2
    else:
        fig2 = px.pie(
            data_frame=df,
            names='jurisdiccion_nombre',
            values='segunda_dosis_cantidad'
        )
    return fig2


@app.callback(  # Figura 3 barras
    Output('bar_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])
def update_graph_bar(value):

    if value == 'primera_dosis_cantidad':
        fig3 = px.bar(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='primera_dosis_cantidad',
            color='primera_dosis_cantidad',
        )

        fig3.update_layout(
            title='Vacunados por covid en primera dosis',
            xaxis_title='Jurisdiccion',
            yaxis_title='Cantidad',

            font=dict(

                size=12,
                color='#7f7f7f'
            ))

        return fig3
    else:
        fig3 = px.bar(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='segunda_dosis_cantidad',
            color='segunda_dosis_cantidad',
        )
    return fig3


# FDigura 4 barras
@app.callback(
    Output('bar_graph2', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])
def update_graph_bar(value):

    if value == 'primera_dosis_cantidad':
        fig3 = px.area(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='primera_dosis_cantidad',
            color_discrete_map={'cantidad': '#E72B1C'},

            labels={'cantidad': 'Cantidad'},

            title='Vacunados por covid en primera dosis',
        )

        fig3.update_layout(
            title='Vacunados por covid',
            xaxis_title='Jurisdiccion',
            yaxis_title='Cantidad',

            font=dict(

                size=12,
                color='#7f7f7f'
            ))

        return fig3
    else:
        fig3 = px.area(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='segunda_dosis_cantidad')
    return fig3


@app.callback(  # Figura 5
    Output('other_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])
def update_graph_bar(value):

    if value == 'primera_dosis_cantidad':
        fig3 = px.line(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='primera_dosis_cantidad',
            color_discrete_map={'cantidad': '#E72B1C'},

            labels={'cantidad': 'Cantidad'},

            title='Vacunados por covid en primera dosis',
        )

        fig3.update_layout(
            title='Vacunados por covid primera dosis ',
            xaxis_title='Jurisdiccion',
            yaxis_title='Cantidad',

            font=dict(

                size=12,
                color='#7f7f7f'
            ))

        return fig3
    else:
        fig3 = px.line(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='segunda_dosis_cantidad')

        fig3.update_layout(
            title='Vacunados por covid en segunda dosis',
            xaxis_title='Jurisdiccion',
            yaxis_title='Cantidad',

            font=dict(

                size=12,
                color='#7f7f7f'
            ))

        return fig3


@app.callback(  # Figura 6
    Output('other_graph2', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])
def update_graph_bar(value):

    if value == 'primera_dosis_cantidad':
        fig3 = px.funnel(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='primera_dosis_cantidad',
            color_discrete_map={'cantidad': '#E72B1C'},

            labels={'cantidad': 'Cantidad'},

            title='Vacunados por covid en primera dosis',
        )

        fig3.update_layout(
            title='Vacunados por covid primera dosis ',
            xaxis_title='Jurisdiccion',
            yaxis_title='Cantidad',

            font=dict(

                size=12,
                color='#7f7f7f'
            ))

        return fig3
    else:
        fig3 = px.funnel(
            data_frame=df,
            x='jurisdiccion_nombre',
            y='segunda_dosis_cantidad')

        fig3.update_layout(
            title='Vacunados por covid en segunda dosis',
            xaxis_title='Jurisdiccion',
            yaxis_title='Cantidad',

            font=dict(

                size=12,
                color='#7f7f7f'
            ))

        return fig3




if __name__ == ('__main__'):
    app.run_server(debug=True)
