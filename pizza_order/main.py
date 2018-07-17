import jinja2
import os
import webapp2


jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Page where user can make an order for pizza.
class OrderHandler(webapp2.RequestHandler):
    # Take the user's order.
    def get(self):
        template = jinja_current_directory.get_template('templates/take_order.html')
        self.response.write(template.render())

# Page with info about our Pizza Service.
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This pizza does not stain your keyboard!')

# Everything from localhost:8080* is routed here (except static_files).
app = webapp2.WSGIApplication([
  # Route localhost:8080/ to OrderHandler.
  ('/', OrderHandler),
  # Route localhost:8080/about to AboutHandler.
  ('/about', AboutHandler),
], debug=True)
