import dash
from dash import Dash, dcc, html
import dash_table
import pandas as pd
import sqlite3

# Create the Dash app
app = dash.Dash()

app.layout = html.Div([
    # Add a dropdown component to select the table
    dcc.Dropdown(
        id='table-select',
        options=[
            {'label': 'Income Statement', 'value': 'income_statement'},
            {'label': 'Balance Sheet', 'value': 'balance_sheet'},
            {'label': 'Profit and Loss', 'value': 'pnl'},
            {'label': 'Government Policies', 'value': 'Goverment_Policies'},
        ],
        value='income_statement'
    ),
    # Add a div to hold the tables
    html.Div(style={'display': 'flex', 'justify-content': 'space-between'}, children=[
        # Add the Table component to display the table
        html.Div(children=dcc.Loading(
            id='table',
            children=dash_table.DataTable(id='table-display'),
            type='default'
        )),
        # Add the Table component to display the Company_Allocation table
        html.Div(children=[
            html.H2('Company Allocation'),
            dcc.Loading(
                id='company-allocation-table',
                children=dash_table.DataTable(
                    id='company-allocation-display',
                    columns=[
                        {'name': 'ID', 'id': 'id'},
                        {'name': 'Country', 'id': 'country'},
                        {'name': 'Industry', 'id': 'industry'},
                        {'name': 'Product', 'id': 'product'},
                    ],
                    data=[],
                    style_cell={'textAlign': 'left'}
                ),
                type='default'
            )
        ])
    ])
])


# Define a callback function to update the table based on the selected table
# Define a callback function to update the table based on the selected table
@app.callback(
    dash.dependencies.Output('table-display', 'data'),
    [dash.dependencies.Input('table-select', 'value'),
     dash.dependencies.Input('company-allocation-display', 'selected_rows')]
)
def update_table(table_name, selected_rows):
    if selected_rows:
        # If a row in the Company_Allocation table is selected, filter the data by the ID
        id = selected_rows[0]
        # Connect to the database and retrieve the data
        con = sqlite3.connect('Financials.db')
        df = pd.read_sql_query(f'SELECT * FROM {table_name} WHERE id=?', con, params=(id,))
        con.close()
    else:
        # If no row is selected, retrieve all the data
        # Connect to the database and retrieve the data
        con = sqlite3.connect('Financials.db')
        df = pd.read_sql_query(f'SELECT * FROM {table_name}', con)
        con.close()
    # Convert the data to a list of dictionaries for the DataTable component
    data = df.to_dict('records')
    return data

# Define a callback function to update the Company_Allocation table
@app.callback(
    dash.dependencies.Output('company-allocation-display', 'data'),
    [dash.dependencies.Input('company-allocation-display', 'selected_rows')]
)
def update_company_allocation(selected_rows):
    if selected_rows:
        # If a row in the Company_Allocation table is selected, filter the data by the ID
        id = selected_rows[0]
        # Connect to the database and retrieve the data
        con = sqlite3.connect('Financials.db')
        df = pd.read_sql_query('SELECT * FROM Company_Allocation WHERE id=?', con, params=(id,))
        con.close()
    else:
        # If no row is selected, retrieve all the data
        # Connect to the database and retrieve the data
        con = sqlite3.connect('Financials.db')
        df = pd.read_sql_query('SELECT * FROM Company_Allocation', con)
        con.close()
        # Convert the data to a list of dictionaries for the DataTable component
    data = df.to_dict('records')
    return data


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8000)