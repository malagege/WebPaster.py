import webapp2

class webPaster(webapp2.RequestHandler):
    def get(self):
        with open("index.html") as f:
            html = f.read()
        self.response.write(html)

    def post(self):
        import win32clipboard
        print self.request.POST["text"]
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(self.request.POST["text"])
        win32clipboard.CloseClipboard()


class getClipboard(webapp2.RequestHandler):
    def get(self):
        import win32clipboard
        win32clipboard.OpenClipboard()
        self.response.write(win32clipboard.GetClipboardData())
        win32clipboard.CloseClipboard()



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