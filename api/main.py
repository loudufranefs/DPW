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
from pageTemplate import PageTemplate

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #access template that will display the form
        p = FormTemplate()
        
        ### IF REQUEST WILL GO HERE ONCE THERE"S A FORM
        
        im = IpModel() #model instance
        im.callApi() #connects to the API
        
        iv = IpView() #view instance
        iv.view_array = im.model_array # data from model inserted into them into the view object
        #add content generated in View object to the page content
        p._page_content = iv.content
        
        
        self.response.write(p.display_page())



#INHERITENCE
#this class will hold the the form,
#it inherits from the pageTemplate class.
class FormTemplate(PageTemplate):
    def __init__(self):
        #constructor function for super class
        super(FormTemplate, self).__init__()
        #attribute for starting the form
        self._form_start = '<form method="GET">'
        #attribute for ending the form
        self._form_end = '</form>'
        
        #array to hold form fields
        self.__form_inputs = []
        
        #build form from form attributes
        self._form = self._form_start + self.__form_inputs + self._form_end
    
    @property #getter for input fields
    def inut_fields(self)
        pass
    
    @input_fields.setter #setter for input fields
    def inut_fields(self, fields_array)
        pass
        
    #POLYMORPHISM - method overriding
    def display_page(self):
        return self._page_head + self._form + self._page_content + self._page_foot

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
