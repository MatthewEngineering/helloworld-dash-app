# dash_hello_world.py
"""
Simple Dash "Hello, World!" app.

Install dependencies:
    pip install dash

Run:
    python dash_hello_world.py

Then open http://127.0.0.1:8050 in your browser.
"""

from dash import Dash, html, Input, Output

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Hello, World!"),
        html.Button("Click me", id="btn", n_clicks=0),
        html.Div(id="output")
    ],
    style={"fontFamily": "Arial, sans-serif", "textAlign": "center", "marginTop": "50px"}
)


@app.callback(Output("output", "children"), Input("btn", "n_clicks"))
def update(n_clicks):
    if n_clicks:
        return f"Button clicked {n_clicks} time{'s' if n_clicks != 1 else ''}!"
    return "Button not clicked yet."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
