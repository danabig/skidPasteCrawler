from urllib.request import urlopen, Request
import os
import json
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


@app.route(API_PATH, methods=['GET', 'POST'])
def request_handler():
    db = DBHandler(DB_PATH)
    data = request.form.to_dict()
    newItem = {'username':data['username'],'data':getContent(data)}
    # linkedInUsers.append(newProfile)
    db.addItem(newItem)
    return Response(json.dumps(newItem['data'][0]), mimetype='application/json', headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})

def getContent(data):
    urlcomplete = BASE_URL #+data['username']
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = { 'User-Agent' : user_agent }
    req = Request(urlcomplete, headers=headers)
    response = urlopen(req)
    return parseItem(response)

def parseItem(response):
    htmlText = response.read()
    parser = MyHTMLParser(htmlText)
    return parser.getJson()

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",8001)))

