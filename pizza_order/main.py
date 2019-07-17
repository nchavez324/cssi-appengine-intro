import jinja2
import os
import webapp2

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Page where user can make an order for pizza.
class TakeOrderHandler(webapp2.RequestHandler):
    # Take the user's order.
    def get(self):
        template = jinja_env.get_template('templates/take_order.html')
        self.response.write(template.render())

# Page where user can view the order they've submitted.
class SubmitOrderHandler(webapp2.RequestHandler):
    # TODO
    pass

# Page with info about our Pizza Service.
class AboutHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('This pizza does not stain your keyboard!')

app = webapp2.WSGIApplication([
  # Route localhost:8080/ to TakeOrderHandler.
  ('/', TakeOrderHandler),
  # Route localhost:8080/submit_order to SubmitOrderHandler.
  ('/submit_order', SubmitOrderHandler),
  # Route localhost:8080/about to AboutHandler.
  ('/about', AboutHandler),
], debug=True)
