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
from view import IpView #import View Class
from controller import IpData #import Controller Class
from model import IpModel #import Model Class

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #access template that will display the form
        p = FormTemplate()
        self.response.write(p.display_page())
        
        #access Model
        im = IpModel()
        #access View
        iv = IpView()
        #access Controller
        ic = IpData()
        
        

        
        
        



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
