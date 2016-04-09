import json
from Request_Handler import Request_Handler
from DBHandler import DBHandler
from MyHTMLParser import MyHTMLParser
from flask import Response, request

BASE_URL = 'http://skidpaste.org/pastes.html'
DB_PATH = 'pastes.json'


class MyServer:
    def __init__(self):
        self.requestHandler = Request_Handler()
        self.index = 0

    def handle_crawl_request(self):
        db = DBHandler(DB_PATH)
        data = request.form.to_dict()
        newItem = {'username':data['username'],'data':self.getContent(data)}
        db.addItem(newItem)
        returnItem = newItem['data'][0]
        return returnItem

    def handle_next_request(self):
        db = DBHandler(DB_PATH)
        itemsList = db.getItemsList()
        listSize = len(itemsList)
        self.index = (self.index + 1) % listSize
        returnItem = itemsList[0]['data'][self.index]
        return returnItem

    def getContent(self,data):
        urlcomplete = BASE_URL #+data['username']
        htmlResponse = self.requestHandler.request(urlcomplete)
        return self.parseItem(htmlResponse)

    def parseItem(self, htmlText):
        parser = MyHTMLParser(htmlText, self.requestHandler)
        return parser.getJson()
