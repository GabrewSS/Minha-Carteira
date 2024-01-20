from dash import html, dcc 
from dash.dependencies import Input, Output, State
from datetime import datetime, date
import dash_bootstrap_components as dbc
import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import calendar
from app import app 



#-----layout------#

layout = dbc.Col([
        html.H5("Página de Dashboards")

])