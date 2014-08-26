'''
Name: Loubna Dufrane
Date: 8/26/2014
Assignment: API
Class: Design Patterns for Web Programming
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
