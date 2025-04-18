from dash import html, dcc

# Visualization Layout
layout_visualization = html.Div([
    html.H3("Visualization"),
    # Element to output plotly chart
    dcc.Graph(id='output-data')
])
