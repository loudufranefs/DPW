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