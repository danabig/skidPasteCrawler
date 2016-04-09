import json


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
        print(self.pastesData)
        jsonObj = json.dumps(self.pastesData)
        with open(self.dbpath, 'w') as file:
            file.write(jsonObj)
        print("db set")