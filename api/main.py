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
        formPage = FormTemplate()
        self.response.write(formPage.displayPage())
        

        #proof of concept code
        
        #get values from API url
        #I am using another API, still the same concept as the proof of concept
        #however this API allows me to get at least 6 pieces of information
        #where as the first API I used only had 5 relevant pieces of data.
        '''
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
        '''
        
        
#VIEW
#-display form
#-display received data
class IpView(object):
    def __init__(self):
        pass

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
        <link href="css/style.css"/>
    </head>
    <body>
    <h2>IP info</h2>
        '''
        #page footer
        self._page_foot = '''
    </body>
</html>
        '''
    #function to display html
    def displayPage(self):
        return self._page_head + self._page_foot
        
        
#INHERITENCE
#this class will hold the the form,
#it inherits from the pageTemplate class.
class FormTemplate(PageTemplate):
    def __init__(self):
        
        #constructor function for super class
        super(FormTemplate, self).__init__()
        
        #setting up form
        self._form_start ='<form>'
        self._form_end ='</form>'
        
        #POLYMORPHISM
        #overriding function
        def displayPage(self):
            return self._page_head + 'test' + self._page_foot

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
