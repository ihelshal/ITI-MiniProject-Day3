# In[]: import packages
import os

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# In[]: Application Creation

app = dash.Dash(__name__)

# In[]: Function to generate the HTML content from each file in explration


def generate_figure_html(file):
    with open(file, "r") as f:
        figure_html = f.read()
        return figure_html


app.layout = html.Div(
    [
        html.H1("Plotly Figures"),
        html.Div(id="figures"),
        dcc.Interval(id="interval-component", interval=60 * 1000, n_intervals=0),
    ]
)

# In[]:

path = "/Users/ihelshal/Kaggle/ITI/PythonDS/ITI-MiniProject-Day3/iframe_figures/"
html_file = [path + file for file in os.listdir(path) if file.endswith(".html")]


# In[]:


@app.callback(
    Output("figures", "children"), [Input("interval-component", "n_intervals")]
)
def update_figures(n_intervals):
    figures = []
    for file in html_file:
        figure_html = generate_figure_html(file)
        figures.append(
            html.Div([html.Iframe(srcDoc=figure_html, width="100%", height="600")])
        )
    return figures


# In[]:

if __name__ == "__main__":
    app.run_server(debug=True)
