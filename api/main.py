'''
Name: Loubna Dufrane
Date: 8/26/2014
Assignment: API
Class: Design Patterns for Web Programming
'''

#Assignment Notes
#collect at least one piece of information
#user can reset/submit - no back button
#validate user input (only if Get exists)

import webapp2
import urllib2 #importing urllib2 for url_info
from xml.dom import minidom #importing minidom of parsing
from view import IpView #import View Class
from controller import IpData #import Controller Class
from model import IpModel #import Model Class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = FormTemplate()
        self.response.write(p.display_page())
        
        
        #get values from API url

        #api_url = "http://ip-api.com/xml/73.55.157.119"
        api_url = "http://api.hostip.info/?ip=12.215.42.19"
        #create request using urllib2 library for api url
        api_request = urllib2.Request(api_url)
        #create api object opener
        api_opener = urllib2.build_opener()
        #get info from api url
        api_result = api_opener.open(api_request)

        #use minidom to parse xml
        apixml = minidom.parse(api_result)
        
        list = apixml.getElementsByTagName('gml:featureMember')
        self.response.write(list)
        '''
        for item in list:
            do = IpData()
            do.country = item.getNamedItem('countryName').nodeValue
            self.response.write(do.country)
        '''

        '''
        #setting up variables for return values temporarily
        timezone = apixml.getElementsByTagName('timezone')[0].firstChild.nodeValue
        lon = apixml.getElementsByTagName('lon')[0].firstChild.nodeValue
        lat = apixml.getElementsByTagName('lat')[0].firstChild.nodeValue
        zipcode = apixml.getElementsByTagName('zip')[0].firstChild.nodeValue
        city = apixml.getElementsByTagName('city')[0].firstChild.nodeValue
        country = apixml.getElementsByTagName('country')[0].firstChild.nodeValue
        '''

#ABSTRACT CLASS
#this class will hold the page template
#it will be used as a super class only
class PageTemplate(object):
    def __init__(self):
        #page_header
        self._page_head = '''<!doctype html>
<html>
    <head>
        <title>IP Info</title>
        <link rel="stylesheet" href="css/style.css" type="text/css" />
    </head>
    <body>
    <h2>IP info</h2>
        '''
        #empty variable to hold page content
        self._page_content =''
        #page footer
        self._page_foot = '''
    </body>
</html>
        '''
    #function to display html
    def display_page(self):
        return self._page_head + self._page_foot
        
        
#INHERITENCE
#this class will hold the the form,
#it inherits from the pageTemplate class.
class FormTemplate(PageTemplate):
    def __init__(self):
        #constructor function for super class
        super(FormTemplate, self).__init__()
        self._form_start = '<form method="GET">'
        self._form_inputs = '''
        input fields will go here
        '''
        self._form_end = '</form>'
        
        #build form from form attributes
        self._form = self._form_start + self._form_inputs + self._form_end
        
    #POLYMORPHISM - method overriding
    def display_page(self):
        return self._page_head + self._form + self._page_foot

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
