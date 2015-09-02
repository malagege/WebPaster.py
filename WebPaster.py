import webapp2
import pyperclip

class webPaster(webapp2.RequestHandler):
    def get(self):
        with open("index.html") as f:
            html = f.read()
        self.response.write(html)

    def post(self):
        pyperclip.copy(self.request.POST["text"])


class getClipboard(webapp2.RequestHandler):
    def get(self):
        self.response.write(pyperclip.paste())


app = webapp2.WSGIApplication([
    ('/', webPaster),
    ('/sentText', webPaster),
    ('/getText', getClipboard),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='8080')

if __name__ == '__main__':
    main()