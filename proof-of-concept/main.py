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
        #instance of page template
        p = PageTemplate()
        self.response.write(p.whole_page)
        
        #get values from API url with hardcoded value
        api_url = "http://netflixroulette.net/api/api.php?title=Bodyguard"
        #create request using urllib2 library for api url
        api_request = urllib2.Request(api_url)
        #create api object opener
        api_object_opener = urllib2.build.opener()

#Page template holding and building html
class PageTemplate(object):
    def __init__(self):
    
        #page head html
        self.page_head='''<!doctype html>
<html>
    <head>
    <title></title>
    </head>
    <body>
    <h1>Netflix Roulette</h1>
        '''
        #page content
        self.page_content=''
        #page end html
        self.page_end='''
    </body>
</html>
        '''
        #build out html page
        self.whole_page = self.page_head + self.page_content + self.page_end

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
