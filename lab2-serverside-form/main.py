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
        <title>{page_title}</title>
        <link rel="stylesheet" href="css/style.css" type="text/css">
        <!--javascript-->
        <script type="text/javascript">
            function OneWay(){
                if (document.getElementById('oneWayCheck').checked){
                    //show return date field
                    document.getElementById('return_date').style.display = 'none';
                }else{
                    // hide return date field
                    document.getElementById('return_date').style.display = 'block';
                }
            }
        </script>
    </head>
    <body>
        <div>
        <h1>Flight Finder</h1>
        '''
        #display form content
        page_content_form = '''
        <h2>Search Flights</h2>
        <form method="GET">
            <div><label>One Way?</label><input type="checkbox" name="type" onChange="OneWay();" id="oneWayCheck"></div>
            <div><label>From</label><input type="text" name="from_location"></div>
            <div><label>To</label><input type="text" name="to_location"></div>
            <div><label>Depart</label><input type="date" name="depart_date"></div>
            <div id="return_date"><label>Returning</label><input type="date" name="return_date"></div>
            <!-Select->
            <div>
                <label>Persons</label>
                <select name="persons">
                    <option value="1" selected>1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
            </div>
            <input type="submit" name="search_btn" value="Search">
        </form>
        '''

        #display result page content
        page_content_result = '''
        <div class="results_page">
            <h2>Your Flight Information</h2>
        </div>
        '''
        page_footer = '''
        </div>
    </body>
</html>
        '''
        if self.request.GET:
            #change page title
            page_title = 'Your Flight Information'
            page = page_header + page_content_result + page_footer
            self.response.write(page)
        else:
            page_title = 'Search Flights'
            page = page_header + page_content_form + page_footer
            self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
