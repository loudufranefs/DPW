'''
Name: Loubna Dufrane
Date: 9/12/2014
Assignment encapsulated Calculator
Class: Design Patterns for Web Programming
Concept : Weightloss Challenge
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class WeightLossTracker(object)
    def __init__(self)
    self.week1 = 0
    self.week2 = 0
    self.week3 = 0
    self.week4 = 0
    self.__total_weightloss = 0
    self.__avg_weighloss_week = 0

    
    
    
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
