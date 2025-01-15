import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

# import os
import pymongo
import os

# from dashgui req file:
# dash==2.18.2
# pymongo==4.10.1
# gunicorn
# pandas
# dash-tools

# "mongodb+srv://sarabarrows18:mongo@cluster0.vgo9y.mongodb.net/"
mango=os.environ.get("mongo_creds")
client = pymongo.MongoClient(mango
    )
db = client["test-db"]
# Go into one of my database's collection (table)
collection = db["table"]

app=dash.Dash(__name__)
server=app.server

app.layout = html.Div(
    [
        dcc.Input(placeholder='Write name here', id='input-val'),
        html.Button('submit', id='button-id', n_clicks=0),
        html.Div(id='output-val')
    ]
)


@app.callback(
    Output('output-val', 'children'),
    Input('button-id', 'n_clicks'),
    State('input-val', 'value')
)
def callbk(n_clicks, input_val):
    
    if n_clicks > 0 and input_val:
                    

        record = {
            "employee": input_val,
            "department": "engineering",
            "product": "PC",
            "part": "motherboard",
            "quantity": "12",
            "day": "Saturday"
        }

        collection.insert_one(record)
        testing = collection.find_one()

        return f'{input_val} has been entered'
    return ''


if __name__ == '__main__':
    app.run_server(debug=True)