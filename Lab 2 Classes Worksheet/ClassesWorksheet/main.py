import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class Doctor(object):
    def __init__(self):
        self.name = ""
        self.specialty = ""
        self.hospital = ""

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
