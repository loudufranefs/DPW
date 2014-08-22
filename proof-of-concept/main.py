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
        
        #get values from API url with hardcoded value
        api_url = "http://api.hostip.info/?ip=12.215.42.19"
        #create request using urllib2 library for api url
        api_request = urllib2.Request(api_url)
        #create api object opener
        api_opener = urllib2.build_opener()
        #get info from api url
        api_result = api_opener.open(api_request)
        print api_result
        #use minidom to parse xml
        apixml = minidom.parse(api_result)
        p.page_content =str(apixml)
        
        #write html page
        self.response.write(p.whole_page)

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
    <h1>Host IP</h1>
    <p>This is a hardcoded example.</p>
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
