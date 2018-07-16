import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        print("Routed here!")
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Goodnight moon!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
