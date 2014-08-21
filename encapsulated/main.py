'''
Name: Loubna Dufrane
Date: 9/12/2014
Assignment encapsulated Calculator
Class: Design Patterns for Web Programming
Concept : Weightloss Challenge
'''
import webapp2
#import page template
from page import PageTemplate
#import weightlostttracker
from tracker import WeightLossTracker

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #page template
        p = PageTemplate()
        
        #Data Object
        lucy = WeightLossTracker()
        lucy.week1 = 5
        lucy.week2 = 8
        lucy.week3 = 2
        lucy.week4 = 4
        
       #self.response.write("Lucy lost and average of " + str(lucy.avg_weighloss_week) + " pounds per week,  and a total of " + str(lucy.total_weightloss) + " pounds.")
        
        print_page = p.page_head + p.page_body + p.page_end
        self.response.write(print_page)

    
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
