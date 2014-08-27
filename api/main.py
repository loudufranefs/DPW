'''
Name: Loubna Dufrane
Date: 8/26/2014
Assignment: API
Class: Design Patterns for Web Programming
'''

#Assignment Notes
#MVC approach
#collect at least one piece of information
#user can reset/submit - no back button
#validate user input (only if Get exists)
#abstract class (class only used as a template)
#inheritence(sub class)
#polymorphism(sub class overriding a function)

import webapp2
import urllib2 #importing urllib2 for url_info
from xml.dom import minidom #importing minidom of parsing

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        

        #proof of concept code
        
        #get values from API url with hardcoded value
        api_url = "http://ip-api.com/xml/208.80.152.201"
        #create request using urllib2 library for api url
        api_request = urllib2.Request(api_url)
        #create api object opener
        api_opener = urllib2.build_opener()
        #get info from api url
        api_result = api_opener.open(api_request)
        #use minidom to parse xml
        apixml = minidom.parse(api_result)
        
        #setting up variables for return values temporarily
        timezone = apixml.getElementsByTagName('timezone')[0].firstChild.nodeValue
        lon = apixml.getElementsByTagName('lon')[0].firstChild.nodeValue
        lat = apixml.getElementsByTagName('lat')[0].firstChild.nodeValue
        zipcode = apixml.getElementsByTagName('zip')[0].firstChild.nodeValue
        city = apixml.getElementsByTagName('city')[0].firstChild.nodeValue
        country = apixml.getElementsByTagName('country')[0].firstChild.nodeValue
        
        self.response.write(country)
        
#VIEW
#-display form
#-display received data
class IpView(object):
    def __init__(self):
        pass

#abstract Class
#this class will hold the page template
class PageTemplate(object):
    def __init__(self):
        #page_header
        page_head = '''<!doctype html>
<html>
    <head>
        <title>IP Info</title>
        <link href="css/style.css"/>
    </head>
    <body>
        '''
        #page footer
        page_foot = '''
    </body>
</html>
        '''

#MODEL
#-recieve data
class IpModel(object):
    def __init__(self):
        pass


#CONTROLLER
#-hold data
class IpData(object):
    def __init__(self):
        pass


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
