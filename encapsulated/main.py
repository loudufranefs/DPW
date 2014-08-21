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
        
        #Data Object - Lucy
        lucy = WeightLossTracker()
        lucy.week1 = 5
        lucy.week2 = 8
        lucy.week3 = 2
        lucy.week4 = 4
        
        #Data Object - Mark
        mark = WeightLossTracker()
        mark.week1 = 4
        mark.week2 = 3
        mark.week3 = 10
        mark.week4 = 5
        
        #Data Object - Pam
        pam = WeightLossTracker()
        pam.week1 = 6
        pam.week2 = 3
        pam.week3 = 8
        pam.week4 = 2
        
        #Data Object - Paul
        paul = WeightLossTracker()
        paul.week1 = 10
        paul.week2 = 5
        paul.week3 = 8
        paul.week4 = 2
        
        #Data Object - Nick
        nick = WeightLossTracker()
        nick.week1 = 3
        nick.week2 = 4
        nick.week3 = 8
        nick.week4 = 3
        
        p.page_body = '''
        <div class="challengers">
            <ul>
            <li>Lucy <a href="/?week1={lucy.week1}&week2={lucy.week2}&week3={lucy.week3}&week4={lucy.week4}&avg_weightlos={lucy.avg_weighloss_week}&total_weightloss={lucy.total_weightloss}">Lucy's Weighloss</a></li>
            <li>Mark <a href="/?week1={mark.week1}&week2={mark.week2}&week3={mark.week3}&week4={mark.week4}&avg_weightlos={mark.avg_weighloss_week}&total_weightloss={mark.total_weightloss}"">Mark's Weighloss</a></li>
            <li>Pam <a href="/?week1={pam.week1}&week2={pam.week2}&week3={pam.week3}&week4={pam.week4}&avg_weightlos={pam.avg_weighloss_week}&total_weightloss={pam.total_weightloss}"">Pam's Weighloss</a></li>
            <li>Paul <a href="/?week1={paul.week1}&week2={paul.week2}&week3={paul.week3}&week4={paul.week4}&avg_weightlos={paul.avg_weighloss_week}&total_weightloss={paul.total_weightloss}"">Paul's Weighloss</a></li>
            <li>Nick <a href="/?week1={nick.week1}&week2={nick.week2}&week3={nick.week3}&week4={nick.week4}&avg_weightlos={nick.avg_weighloss_week}&total_weightloss={nick.total_weightloss}"">Nick's Weighloss</a></li>
            </ul>
        </div>
        '''
        
        print_page = p.page_head + p.page_body + p.page_end
        self.response.write(print_page.format(**locals()))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
