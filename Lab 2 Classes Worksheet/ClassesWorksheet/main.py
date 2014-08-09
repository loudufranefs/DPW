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
        self._name = ""
        self._medical_field = ""
        self._hospital_name = ""
        self._amount_patients = ""
        
    def diagnose_patient(self):
        pass
    def visit_patient(self):
        pass
    def run_analysis(self):
        pass

class Nurse(object):
    def __init__(self):
        self._name = ""
        self._type = ""
        self._hospital_name = ""
        self._hospital_floor = ""

    def check_patient(self):
        pass
    def give_medication(self):
        pass
    def transfer_patient(self):
        pass

class Patient(object):
    def __init__(self):
        self._name = ""
        self._hospital_name = ""
        self._hospital_room = ""
        self._age = ""
        self._medical_issue = ""
        self._hospital_entry_date = ""
        self._hospital_release_date = ""

    def take_medication(self):
        pass
    def sleep(self):
        pass
    def call_nurse(self):
        pass

class Visitor(object):
    def __init__(self):
        self._name = ""
        self._patient_visiting = ""
        self._hospital_room = ""
        self._date_visiting = ""

    def visit_patient(self):
        pass
    def buy_flowers(self):
        pass
    def sympathise(self):
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
