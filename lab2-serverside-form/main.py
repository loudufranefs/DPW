'''
Name: Loubna Dufrane
Date: 9/12/2014
Assignment: Lab 2 Server Side Form (Simple Form)
Class: Design Patterns for Web Programming
Concept : form for booking a flight
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_header = ''
        page_form = ''
        page_footer = ''

        page = ''
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
