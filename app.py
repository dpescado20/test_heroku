from flask import Flask

import dash_html_components as html

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

@app.route('/flask')
def hello_world():
    return 'Hello World'

app.layout = html.Div([html.H2('Hello World)])

if __name__ == '__main__':
    app.run_server()
