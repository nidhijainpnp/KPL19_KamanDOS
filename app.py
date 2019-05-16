import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from one import closest_five
from two import plot
from three import func


# 'https://codepen.io/chriddyp/pen/bWLwgP.css', 
external_stylesheets = []

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', className="main")
])


index_page = html.Div([
    html.H1('KPL Hackathon'),
    html.Br(),
    dcc.Link(html.Button('Go to Problem 1', className="waves-effect waves-light btn-large"), href='/problem1', className="prob_buttons"),
    html.Br(),
    html.Br(),
    dcc.Link(html.Button('Go to Problem 2', className="waves-effect waves-light btn-large"), href='/problem2', className="prob_buttons"),
    html.Br(),
    html.Br(),
    dcc.Link(html.Button('Go to Problem 3', className="waves-effect waves-light btn-large"), href='/problem3', className="prob_buttons"),
])


problem1_layout = html.Div([
    html.H1('Problem 1'),
    dcc.Input(
        id='problem1-input',
        type='number',
        value='',
        placeholder="Star ID"
    ),
    html.Div(id='problem1-content'),
    html.P('No star is above horizon.'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])


@app.callback(dash.dependencies.Output('problem1-content', 'children'),
              [dash.dependencies.Input('problem1-input', 'value')])
def problem1_input(value):
    if value == '':
        return ""
    try:
        _, ans = closest_five(int(value))
    except:
        return "Invalid value. Please try again."
    return html.Table(
        [html.Tr([html.Th("ID"), html.Th("Separation")]) ] +
        [html.Tr([
            html.Td(id), html.Td(sep)
        ]) for sep, id in ans],
        className="highlight striped responsive-table centered"
    )


problem2_layout = html.Div([
    html.H1('Problem 2'),
    dcc.Graph(
        id = 'problem2plot',
        figure = {
            'data': plot()[0],
            'layout': go.Layout(
                xaxis={'title': 'Ratio of apparent wavelength and real wavelength'},
                yaxis={'title': 'Distance modulus'},
            )
        }
    ),
    html.P(plot()[1]),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])


problem3_layout = html.Div([
    html.H1('Problem 3'),
    html.Div(
        html.Table(
            [html.Tr([html.Th("ID"), html.Th("E (B-V) Color Index")]) ] +
            [html.Tr([
                html.Td(id), html.Td(sep)
            ]) for sep, id in func()],
            className="highlight striped responsive-table centered"
        ),
        id='problem1-content',
    ),
    html.Br(),
    dcc.Link('Go back to home', href='/'),
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/problem1':
        return problem1_layout
    elif pathname == '/problem2':
        return problem2_layout
    elif pathname == '/problem3':
        return problem3_layout
    else:
        return index_page


if __name__ == '__main__':
    app.run_server(debug=True)