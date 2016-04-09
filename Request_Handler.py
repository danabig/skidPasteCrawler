from urllib.request import urlopen, Request

class Request_Handler:
    def request(self, url):
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = { 'User-Agent' : user_agent }
        req = Request(url, headers=headers)
        response = urlopen(req)
        return response.read()