import unicodedata
from bs4 import BeautifulSoup


class MyHTMLParser:
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')
        self.parsedJson = {"name":[], "title":[],"position":[],"summary":[],"skills":[]}
        self.getskills()
        self.getsummary()
        self.getposition()
        self.gettitle()
        self.getname()

    def gettitle(self):
        titleTag = self.soup.find(class_="headline title")
        if titleTag == None:
            return
        self.parsedJson['title'] = self.convertToString(titleTag.get_text())

    def getname(self):
        nametag = self.soup.find(id="name")
        if nametag == None:
            return
        self.parsedJson['name'] = self.convertToString(nametag.get_text())

    def getposition(self):
        for tr in self.soup.find_all('tr'):
            if tr['data-section'] == "currentPositionsDetails":
                self.parsedJson['position'] = self.convertToString(tr.get_text())
                return

    def getsummary(self):
        summarytag = self.soup.find(id="summary")
        if summarytag == None:
            return
        text = summarytag.get_text()
        self.parsedJson['summary'] = self.convertToString(text)

    def getskills(self):
        skills = []
        skillstag = self.soup.find(id="skills")
        if skillstag == None:
            return
        for span in skillstag.find_all('span'):
            skills.append(self.convertToString(span.get_text()))
        self.parsedJson['skills'] = skills

    def convertToString(self, text):
       return unicodedata.normalize('NFKD', text).encode('ascii','ignore')

    def getJson(self):
        return self.parsedJson