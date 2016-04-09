import urllib2
import os
import json
from MyHTMLParser import MyHTMLParser
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))
BASE_URL='https://www.linkedin.com/in/'
FAKE_URL='http://www.google.com'
FAKE_URL2='https://www.facebook.com/'


@app.route('/api/linkedinsearch', methods=['GET', 'POST'])
def request_handler():
    with open('linkedinUsers.json', 'r') as file:
        linkedInUsers = json.loads(file.read())
    data = request.form.to_dict()
    newProfile = {'username':data['username'],'data':getProfile(data)}
    linkedInUsers.append(newProfile)
    with open('linkedinUsers.json', 'w') as file:
        file.write(json.dumps(linkedInUsers, indent=4, separators=(',', ': ')))
    return Response(json.dumps(newProfile['data']), mimetype='application/json', headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})


@app.route('/api/linkedinsearch/count', methods=['GET', 'POST'])
def request_count_handler():
    with open('linkedinUsers.json', 'r') as file:
        linkedInUsers = json.loads(file.read())
    data = request.form.to_dict()
    topSkillsCount = -1
    for profile in linkedInUsers:
        if profile['username'] == data['username']:
            topSkillsCount = len(profile['data']['skills'])
    return Response(json.dumps({"count":topSkillsCount}), mimetype='application/json', headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})


def getProfile(data):
    urlcomplete = BASE_URL+data['username']
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = { 'User-Agent' : user_agent }
    req = urllib2.Request(urlcomplete, headers=headers)
    response = urllib2.urlopen(req)
    return parseProfile(response)

def parseProfile(response):
    htmlText = response.read()
    parser = MyHTMLParser(htmlText)
    return parser.getJson()

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",8001)))

