'''
Name: Loubna Dufrane
Date: 9/12/2014
Assignment: Lab 2 Server Side Form (Simple Form)
Class: Design Patterns for Web Programming
Concept : form for booking a flight
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_header = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
        <link rel="stylesheet" href="css/style.css" type="text/css">
    </head>
    <body>
        <div>
        '''
        #display form content
        page_content_form = '''
        <form method="GET">
            <div><label>From</label><input type="text" name="from_location></div>
            <div><label>To</label><input type="text" name="to_location></div>
            <div><label>Leaving</label><input type="date" name="leave_date"></div>
            <div><label>Returning</label><input type="date" name="return_date></div>
        </form>
        '''
        #display result page content
        page_content_result = '''
        '''
        page_footer = '''
        </div>
    </body>
</html>
        '''

        page = page_header + page_content_form + page_footer
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
