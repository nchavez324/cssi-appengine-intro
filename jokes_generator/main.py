import jinja2
import os
import webapp2

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('welcome.html')
        template_vars = {
            'greeting': 'Welcome!',
            'available_qualities': ['corny', 'good', 'overused'],
        }
        self.response.write(template.render(template_vars))

class ResultPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('result.html')
        template_vars = {
            'joke_line_1': 'If Cinderella\'s shoe was a perfect fit',
            'joke_line_2': 'Then why did it fall off?',
            'image_url': '/static/thatsthejoke.jpg',
            'joke_is_good': True,
        }
        self.response.write(template.render(template_vars))

class SignupPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('signup.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/result', ResultPage),
    ('/signup', SignupPage),
], debug=True)
