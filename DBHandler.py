import json
# DB_FILE = 'pastes.json'

class DBHandler:
    def __init__(self, path):
        self.dbpath = path;
        self.pastesData = []
        self.loadDB();

    def loadDB(self):
        with open(self.dbpath, 'r') as file:
            self.pastesData = json.loads(file.read())

    def addItem(self, data):
        self.pastesData.append(data)
        self.setDB()

    def setDB(self):
        with open(self.dbpath, 'w') as file:
            file.write(json.dumps(self.pastesData, indent=4, separators=(',', ': ')))