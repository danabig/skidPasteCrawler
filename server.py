import os
import json
from Request_Handler import Request_Handler
from DBHandler import DBHandler
from MyHTMLParser import MyHTMLParser
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))
BASE_URL='http://skidpaste.org/pastes.html'
DB_PATH = 'pastes.json'
FAKE_URL='http://www.google.com'
FAKE_URL2='https://www.facebook.com/'

API_PATH = '/api/pastes'

requestHandler = Request_Handler()

@app.route(API_PATH, methods=['GET', 'POST'])
def request_handler():
    db = DBHandler(DB_PATH)
    data = request.form.to_dict()
    newItem = {'username':data['username'],'data':getContent(data)}
    db.addItem(newItem)
    returnItem = newItem['data'][0]
    return Response(json.dumps(returnItem), mimetype='application/json', headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})

def getContent(data):
    urlcomplete = BASE_URL #+data['username']
    htmlResponse = requestHandler.request(urlcomplete)
    return parseItem(htmlResponse)

def parseItem(htmlText):
    parser = MyHTMLParser(htmlText, requestHandler)
    return parser.getJson()

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",8001)))

