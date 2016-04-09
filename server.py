import os, json
from MyServer import MyServer
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

API_PATH = '/api/pastes'
API_NEXT = '/api/nextPaste'

server = MyServer()

@app.route(API_PATH, methods=['GET', 'POST'])
def request_handler():
    returnItem = server.handle_crawl_request()
    return Response(json.dumps(returnItem), mimetype='application/json', headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})

@app.route(API_NEXT, methods=['GET', 'POST'])
def next_request_handler():
    returnItem = server.handle_next_request()
    return Response(json.dumps(returnItem), mimetype='application/json', headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",8001)))

