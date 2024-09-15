import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_table

# Load your data from CSV
df = pd.read_csv('polotty.csv')

# Convert 'Time' column to a datetime object for proper plotting
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S.%f')

# Print the first few rows and the column names for debugging
print("Data preview:\n", df.head())  # Debug: Check if data is loaded
print("Column names:\n", df.columns)  # Debug: Check column names

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    dcc.Dropdown(
        id='variable-dropdown',
        options=[
            {'label': 'X', 'value': 'X'},
            {'label': 'Y', 'value': 'Y'},
            {'label': 'Z', 'value': 'Z'}
        ],
        value=['X'],  # Default value, can be single or multiple variables
        multi=True  # Allow multiple selections
    ),
    dcc.Input(
        id='sample-input',
        type='number',
        value=100,  # Default number of samples
        placeholder="Enter number of samples"
    ),
    dcc.Dropdown(
        id='graph-type-dropdown',
        options=[
            {'label': 'Line', 'value': 'line'},
            {'label': 'Scatter', 'value': 'scatter'},
            {'label': 'Distribution', 'value': 'dist'}
        ],
        value='line',  # Default to line graph
        placeholder="Select graph type",
    ),
    dcc.Graph(id='gyro-graph'),  # Graph to display the plot
    dash_table.DataTable(
        id='stats-table',  # Table to display summary statistics
        columns=[
            {"name": "Statistic", "id": "stat"},
            {"name": "Value", "id": "value"}
        ]
    )
])

# Callback function to update graph and table
@app.callback(
    [Output('gyro-graph', 'figure'), Output('stats-table', 'data')],
    [Input('variable-dropdown', 'value'), Input('sample-input', 'value'), Input('graph-type-dropdown', 'value')]
)
def update_graph_and_table(variables, sample_size, graph_type):
    # Ensure the selected variables exist in the dataframe
    if not all(var in df.columns for var in variables):
        return px.scatter(), [{"stat": "Error", "value": "Invalid variable selection"}]

    # Filter the dataframe based on selected variables and sample size
    filtered_df = df[['Time'] + variables].head(sample_size)

    # Debugging: Print the filtered data
    print("Filtered data preview:\n", filtered_df.head())  # Debug: Check if data is filtered correctly

    # Handle case where no data is available
    if filtered_df.empty:
        return px.scatter(), [{"stat": "Error", "value": "No data available"}]

    # Select the graph type based on user input
    if graph_type == 'line':
        fig = px.line(filtered_df, x='Time', y=variables)
    elif graph_type == 'scatter':
        fig = px.scatter(filtered_df, x='Time', y=variables)
    else:  # Distribution plot
        fig = px.histogram(filtered_df, x=variables[0], nbins=30)  # Plot distribution for one variable

    # Calculate statistics (mean, min, max, std) for the filtered data
    stats = {
        "Mean": filtered_df[variables].mean().to_dict(),
        "Min": filtered_df[variables].min().to_dict(),
        "Max": filtered_df[variables].max().to_dict(),
        "Std Dev": filtered_df[variables].std().to_dict()
    }
    
    # Prepare the data for the table by converting stats into a list of dicts
    table_data = [{"stat": stat, "value": str(values)} for stat, values in stats.items()]
    
    return fig, table_data

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
