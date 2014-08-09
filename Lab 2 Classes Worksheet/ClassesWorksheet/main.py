'''
Name: Loubna Dufrane
Date: 8/9/2014
Assignment: Lab2 Classes Worksheet
Class: Designing for Web Programming
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
'''
Hospital Scenario
'''
class Doctor(object):
    def __init__(self):
        self.name = ""
        self.medical_field = ""
        self.hospital_name = ""
        self.amount_patients = ""
        
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

    def check_patient(self):
        pass
    def give_medication(self):
        pass
    def transfer_patient(self):
        pass

class Patient(object):
    def __init__(self):
        self.name = ""
        self.hospital_name = ""
        self.hospital_room = ""
        self.age = ""
        self.medical_issue = ""
        self.hospital_entry_date = ""
        self.hospital_release_date = ""

    def take_medication(self):
        pass
    def sleep(self):
        pass
    def call_nurse(self):
        pass

class Visitor(object):
    def __init__(self):
        self.name = ""
        self.patient_visiting = ""
        self.hospital_room = ""
        self.date_visiting = ""

    def visit_patient(self):
        pass
    def buy_flowers(self):
        pass
    def sympathise(self):
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
