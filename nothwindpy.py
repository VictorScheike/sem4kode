import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

Excel_file = 'my_shop_data.xlsx'
EmployeesSale = pd.read_excel(Excel_file, "order")
CategorySale = pd.read_excel(Excel_file, "order")

def employesssale():
    fig = px.scatter(EmployeesSale, x='employee_id', y='order_id', title='Sales by employee')
    return fig    

def categorysale():
    fig = px.scatter(CategorySale, x='product_id', y='order_id', title='Sales by products')
    return fig

app = dash.Dash()

app = dash.Dash(external_stylesheets = [ dbc.themes.FLATLY],)

body_app = dbc.Container([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id = 'employee_id', figure=employesssale()),
            style = {'height':'400px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),
        dbc.Col(
            dcc.Graph(id = 'product_id', figure=categorysale()),
            style = {'height':'400px'},xs = 12, sm = 12, md = 6, lg = 6, xl = 6),
    ]),

],fluid = True) 

topbar = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.NavbarBrand("Delivery 1 - 28-03-2022", style = {'color':'black', 'fontSize':'25px','fontFamily':'Times New Roman'}
                    ),
                )
            ],
            align="center",
            className="g-10",
        ),
    ]
)

app.layout = html.Div(id = 'parent', children = [topbar, body_app])

if __name__ == "__main__":
    app.run_server()