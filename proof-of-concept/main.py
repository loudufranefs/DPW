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
        
        
        #use minidom to parse xml
        apixml = minidom.parse(api_result)
        
        #target element named IP
        ip = apixml.getElementsByTagName('ip')[0].firstChild.nodeValue
        #target element named "countryName"
        country_name = apixml.getElementsByTagName('countryName')[0].firstChild.nodeValue
        
        #write content with country_name to page content
        p.page_content = "The IP address: <u>" + ip + "</u> address is in country: <strong>" + str(country_name) + "</strong>"
        
        #build out html page
        p.whole_page = p.page_head + p.page_content + p.page_end
        #render html page
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
    <p>This API looks up location by IP address. The API can be found here: <a href="http://www.hostip.info/use.html">http://www.hostip.info/use.html</a></p>
    <p>This is a hardcoded example.</p>
        '''
        #page content
        self.page_content=''
        #page end html
        self.page_end='''
    </body>
</html>
        '''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
