from bs4 import BeautifulSoup


class MyHTMLParser:
    def __init__(self, html_doc):
        self.soup = BeautifulSoup(html_doc, 'html.parser')
        self.pastes = []
        self.parsedJson = {"url":[], "title":[],"content":[]}
        self.getdetails()

    def getdetails(self):
        leftSideTag = self.soup.find(id="content_left")
        for tr in leftSideTag.find_all('tr'):
            a = tr.find('a')
            if a != None:
                title = a.get_text()
                paste = {"title": title}
                self.pastes.append(paste)

    def getJson(self):
        return self.pastes