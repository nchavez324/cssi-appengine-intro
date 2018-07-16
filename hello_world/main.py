import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, Im Nick!')

class AboutPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('<html>I work at Google!</html>!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/about', AboutPage)
], debug=True)
