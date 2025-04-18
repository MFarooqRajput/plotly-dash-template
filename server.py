from dash import Dash

app = Dash(__name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    ]
)
