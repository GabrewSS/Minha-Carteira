import os
import dash
from dash import html, dcc 
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app 

from datetime import datetime, date
import plotly.express as px
import numpy as np 
import pandas as pd





#------------------Layout----------------#

layout = dbc.Col ([
                html.H1("Financeiro Mila & Gabrew", className="text-primary"),
                html.P("By Asimov", className="text-info"),
                html.Hr(),

#----seleção de perfil------#

                dbc.Button(id="botao_perfil" ,
                    children=[html.Img(src="/imagens/Gabrew.jpeg", id="perfil_change", alt="Perfil", className="perfil_perfil")
                ], style={"backgroud-color": "transparent", "border-color": "transparent"}),

            
#-----seção de novo-------#

                dbc.Row([
                    dbc.Button(color="sucess", id="abrir_nova_receita",
                                children=["+ Receita"])
                    ], width=6),
                dbc.Row([
                    dbc.Button(color="danger", id="abrir_nova_despesa",
                                children=["- Despesa"])
                    ], width=6),
                #----modal receita----#
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Dinheiro Entrando")),
                    dbc.ModalBody([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Descrição: "),
                                dbc.Input(placeholder="Ex.: Sálario, Vale..", id="txt-receita"),
                            ], width=6),
                            dbc.Col([
                                dbc.Label("Valor: "),
                                dbc.Input(placeholder="$100.00", id="valor_receita", value="")
                            ])
                        ])

                    ])
                ], id= "modal-nova-receita"),
                #----modal despesa----#
                dbc.Modal([
                    dbc.ModalHeader(dbc.ModalTitle("Dinheiro Saindo")),
                    dbc.ModalBody([

                    ])
                ], id="modal-nova-despesa"),

#----seção navegação------#
                html.Hr(),
                dbc.Nav(
                [
                    dbc.NavLink("Deshboard", href="/dashboards", active="exact"),
                    dbc.NavLink("Extratos", href="/extratos", active="exact"),
                ], vertical=True, pills=True, id="nav_buttons", style={"margin-buttom": "50px"}),
                

            ], id="sidebar_completa")    







#----seção Callbacks----#
#---pop up receita----#
@app.Callbacks(
    Output("modal-nova-receita", "is_open"),
    Input("abrir-nova-receita", "n_clics"),
    State("modal-nova-receita", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    
#---pop up despesa----#
@app.Callbacks(
    Output("modal-novo-despesa", "is_open"),
    Input("abrir-novo-despesa", "n_clics"),
    State("modal-novo-despesa", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open            



