import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class Doctor(object):
    def __init__(self):
        self.name = ""
        self.specialty = ""
        self.hospital_name = ""
        
    def diagnose_patient(self):
        pass
    def visit_patient(self):
        pass
    def run_analysis(self):
        pass

class Nurse(object):
    def __init__(self):
        self.name = ""
        self.type = ""
        self.hospital_name = ""
        self.hospital_floor = ""


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
