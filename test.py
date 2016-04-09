import json
from LinkedHTMLParser import LinkedHTMLParser
from MyHTMLParser import MyHTMLPArser

txt = open('linkedIn.htm')
parser = MyHTMLPArser(txt)
# parser.feed(txt.read())
newProfile = parser.getJson()
# print json.dumps(parser.getJson(),indent=4, separators=(',', ': '))
with open('linkedinUsers.json', 'r') as file:
    linkedInUsers = json.loads(file.read())
linkedInUsers.append(newProfile)
with open('linkedinUsers.json', 'w') as file:
    file.write(json.dumps(linkedInUsers, indent=4, separators=(',', ': ')))

print json.dumps(linkedInUsers,indent=4, separators=(',', ': '))
