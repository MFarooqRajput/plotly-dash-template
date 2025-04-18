import numpy as np
from server import app
from dash import Input, Output
import plotly.graph_objects as go

def _generate_chart(series):
    # Create a trace
    trace = go.Scatter(
        y=series,
        mode='lines'
    )

    data = [trace]

    fig = {
        'data': data,
        'layout': {
            'margin': {'l': 40, 'r': 40, 't': 40, 'b': 40}
        }
    }
    return fig

@app.callback(
    Output('output-data', 'figure'),
    Input('input-mean', 'value'),
    Input('input-stdv', 'value')
)
def update_visualization(mean, stdv):
    mean = mean if mean is not None else 0
    stdv = stdv if stdv is not None else 1
    # Generates a random sample from a Normal Distribution
    time_series = np.random.normal(mean, stdv, 1000)
    # Generates a plotly chart
    chart_layout = _generate_chart(time_series)
    return chart_layout
