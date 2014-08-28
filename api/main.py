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
        #array of input fields
        p.input_fields = [['ip', 'text', 'IP Address'],['submit', 'submit']]
        
        #Only if there's a GET
        if self.request.GET:
            im = IpModel() #model instance
            im.ip = self.request.GET['ip'] #get IP from URL
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
        #attribute will be used to form the html from the form_inputs array
        self._inputs =''
        
    
    @property #getter for input fields
    def input_fields(self):
        pass
    
    @input_fields.setter #setter for input fields
    def input_fields(self, fields_array):
        #settings the value to the value coming in through the function.
        self.__form_inputs = fields_array
        
        #looping through the array to generate html for input fields
        for item in fields_array:
            #generate input field
            self._inputs +='<input type="' + item[1] + '" name="' + item[0] + '"'
            #check if there's item[2] and generate the rest of the input field
            try:
                self._inputs += ' placeholder="' + item[2] + '" />'
            #otherwise end the input field tag
            except:
                self._inputs +=' />'
            
    
        
    #POLYMORPHISM - method overriding
    def display_page(self):
        return self._page_head + self._form_start + self._inputs + self._form_end + self._page_content + self._page_foot
    
    

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
