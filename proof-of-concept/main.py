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
    
        #page head html
        self.page_head='''<!doctype html>
<html>
    <head>
    <title></title>
    </head>
    <body>
    '''
        #page content
        self.page_content='''
    '''
        #page end html
        self.page_end='''
    </body>
</html>
    '''
    
        def build_page(self):
            return self.page_head + self.page_content + self.page_end

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
