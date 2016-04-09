import unicodedata
from bs4 import BeautifulSoup

SKIDPASE_BASEURL = 'http://skidpaste.org/'

class MyHTMLParser:
    def __init__(self, html_doc, requestHandler):
        self.soup = BeautifulSoup(html_doc, 'html.parser')
        self.requestHandler = requestHandler
        self.pastes = []
        self.parsedJson = {"url":[], "title":[],"content":[]}
        self.getdetails()

    def getdetails(self):
        limit = 10
        leftSideTag = self.soup.find(id="content_left")
        for tr in leftSideTag.find_all('tr'):
            if limit == 0:
                return
            limit -= 1
            print("parsing paste")
            a = tr.find('a')
            if a != None:
                title = a.get_text()
                url = SKIDPASE_BASEURL+a['href']+'.txt'
                textChunc = self.requestHandler.request(url)
                contentText = self.convertByteToString(textChunc)
                paste = {"title": title, 'url': url, 'content': contentText}
                self.pastes.append(paste)

    def getJson(self):
        return self.pastes

    def convertByteToString(self, text):
       # txt = unicodedata.normalize('NFKD', text).encode('ascii','ignore')
       txt = text.decode(encoding='UTF-8')
       print('convert')
       return txt
