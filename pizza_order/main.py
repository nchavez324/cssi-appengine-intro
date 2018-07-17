import jinja2
import os
import webapp2


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Page where user can make an order for pizza.
class OrderHandler(webapp2.RequestHandler):
    def get(self):
        input_template = jinja_current_directory.get_template('templates/input_order.html')
        self.response.write(input_template.render())

# Page with info about our Pizza Service.
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This pizza does not stain your keyboard!')

app = webapp2.WSGIApplication([
  ('/', OrderHandler),
  ('/about', AboutHandler),
], debug=True)
