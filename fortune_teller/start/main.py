import webapp2
import os
import random
import jinja2


def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list=[
      'You will be $2 richer next week',
      'You will live very long',
      'Lucky numbers 42, 101, and 99',
      'You will get a puppy for the holidays!',
      'The Mets will win next year',
    ]
    #use the random library to return a random element from the array
    random_fortune = random.randint(0, len(fortune_list) - 1)
    return(fortune_list[random_fortune])


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        self.response.write(get_fortune())
    #add a post method
    #def post(self):

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_current_directory.get_template('welcome.html')
        self.response.write(template.render())

class TermsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_current_directory.get_template('terms.html')
        self.response.write(template.render())

#the route mapping
app = webapp2.WSGIApplication([
    ('/', HelloHandler),
    ('/terms', TermsHandler),
    ('/predict', FortuneHandler) #maps '/predict' to the FortuneHandler
], debug=True)
