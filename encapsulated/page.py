class PageTemplate(object):
    def __init__(self):
        #page head holding beginning html
        self.page_head ='''<!doctype html>
<html>
    <head>
    <title>Weightloss Challenge</title>
    <link rel="stylesheet" href="css/style.css" type="text/css" />
    </head>
    <body>
        <div id="wrapper">
            <h1>Weightloss Challenge</h1>
        '''
        #page body holding content
        self.page_body = ''' No Challengers to display
        '''
    
        #page end holding end html
        self.page_end = '''
        </div>
    </body>
</html>
        '''
    
    