'''
Name: Loubna Dufrane
Date: 9/12/2014
Assignment: Lab 2 Server Side Form (Simple Form)
Class: Design Patterns for Web Programming
Template: PageTemplate
'''
#page Template setup
class PageTemplate(object):
    def __init__(self):
        #page header holding the html head, linking to the stylesheet and includes javascript that makes the form interactive by showing/hiding one of the form fields.
        self.page_header = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Flight Finder</title>
        <!-- CSS-->
        <link rel="stylesheet" href="css/style.css" type="text/css">
        <!--javascript-->
        <script type="text/javascript">
            function OneWay(){
                if (document.getElementById('oneWayCheck').checked){
                    //hide return date field
                    document.getElementById('return_date').style.display = 'none';
                }else{
                    document.getElementById('oneWayCheck').value = "false";
                    // show return date field
                    document.getElementById('return_date').style.display = 'block';
                }
            }
        </script>
    </head>
    <body>
        <div>
        <h1>Flight Finder</h1>
        '''
        #page content showing the form fields and submit button. This variable will be overwritten once user submits form and will instead show the values instead of the form. I think this is more optimized than adding another variable and showing that instead.
        self.page_content_form = '''
        <h2>Search Flights</h2>
        <form method="GET">
            <div><label>From</label><input type="text" name="from_location"></div>
            <div><label>To</label><input type="text" name="to_location"></div>
            <div><label>Depart</label><input type="date" name="depart_date"></div>
            <div id="return_date"><label>Returning</label><input type="date" name="return_date"></div>
            <span class="clear_all"></span>
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
            <div><label>One Way?</label>
            <input type="checkbox" name="flight_type" onChange="OneWay();" id="oneWayCheck">
            </div>
            <input type="submit" name="search_btn" value="Search">
        </form>
        '''
        #page footer closes the html page.
        self.page_footer = '''
        </div>
    </body>
</html>
        '''