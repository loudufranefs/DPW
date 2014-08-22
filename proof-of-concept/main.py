'''
Name: Loubna Dufrane
Date: 8/21/2014
Assignment Proof of Concept
Class: Design Patterns for Web Programming
'''
import webapp2
import urllib2 #importing urllib2 for url_info
from xml.dom import minidom #importing minidom of parsing

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
        
class PageTemplate(object):
    def __init__(self):
    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
