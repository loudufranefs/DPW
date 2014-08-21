'''
Name: Loubna Dufrane
Date: 9/12/2014
Assignment encapsulated Calculator
Class: Design Patterns for Web Programming
Concept : Weightloss Challenge
'''
import webapp2
#import weightlostttracker
from tracker import WeightLossTracker

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


    
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
