'''
Name: Loubna Dufrane
Date: 9/12/2014
Assignment: Lab 2 Server Side Form (Simple Form)
Class: Design Patterns for Web Programming
Concept : searching for flights
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
            # for the checkbox value to come through when there is no value, I needed to use get_all
            flight_type = self.request.get_all('flight_type')

            #check amount of people and change wording
            if int(persons) > 1:
                persons_flying = 'people'
            else:
                persons_flying = 'person'

            #condition for flight type
            if flight_type == []:
                flight_type = 'Round Trip'
                #show return flight date if it's a round trip
                return_information = '<dt id="return_value">Returning:</dt><dd>' + str(return_date) + ' </dd>'
            else:
                flight_type = 'One Way'
                #no return date with a one way flight
                return_information = ''



            #over-write page content with form values
            pt.page_content_form = '''
        <h2>Your Flight Information</h2>
        <div class="results_page">
            <h3>You want to book a <span>'''+ flight_type + '</span> flight with  <span>'+ persons + ' ' + persons_flying + ''' </span>Traveling</h3>
           <dl>
                <dt>From:</dt><dd> ''' + from_location + ''' </dd>
                <dt>To:</dt><dd> ''' + to_location + ''' </dd>
                <dt>Trip Date:</dt><dd> ''' + str(depart_date) + ''' </dd>
                ''' + return_information + '''
           </dl>
           <h4>Thank you for Flying with us!</h4>
        </div>
        '''
        #page variable to render
        page = pt.page_header + pt.page_content_form + pt.page_footer

        #write html page
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)