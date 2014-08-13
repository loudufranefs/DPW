'''
Name: Loubna Dufrane
Date: 9/12/2014
Assignment: Lab 2 Server Side Form (Simple Form)
Class: Design Patterns for Web Programming
Concept : form for booking a flight
'''

import webapp2

from template import PageTemplate
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Get Page Template
        pt = PageTemplate()

        #Check if GET exists
        if self.request.GET:
            #form field variables to capture data
            to_location = self.request.GET['to_location']
            from_location = self.request.GET['from_location']
            depart_date = self.request.GET['depart_date']
            return_date = self.request.GET['return_date']
            persons = self.request.GET['persons']
            flight_type = self.request.get_all('flight_type')

            #check amount of people and change wording appropriatly
            if int(persons) > 1:
                persons_flying = 'people'
            else:
                persons_flying = 'person'

            #condition for flight type
            if flight_type == 'true':
                flight_type = 'One Way'
            else:
                flight_type = 'Round Trip'
            #over-write page title
            pt.page_title = "Your Flight Information"
            #over-write page content with form values
            pt.page_content_form = '''
        <div class="results_page">
            <h2>Your Flight Information</h2>
            <h3>You want to book a '''+ flight_type + ' flight with  '+ persons + ' ' + persons_flying + ''' Traveling</h3>
           <dl>
                <dt>From:</dt><dd> ''' + from_location + ''' </dd>
                <dt>To:</dt><dd> ''' + to_location + ''' </dd>
                <dt>Departing:</dt><dd> ''' + str(depart_date) + ''' </dd>
                <dt id="return_value">Returning:</dt><dd> ''' + str(return_date) + ''' </dd>
           </dl>
           <h4>Thank you for Flying with us</h4>
        </div>
        '''
        #page variable to render
        page = pt.page_header + pt.page_content_form + pt.page_footer
        #write html page
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
