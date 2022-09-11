from tokenize import String
import pymongo
from mongoengine import *

# define class for mongo db patient record
# see : https://leportella.com/mongoengine/
# Connect to mongo DB
connect('med_data')


class PathologyResults(EmbeddedDocument):
    date = DateField()
    test_name = StringField()
    result = FloatField()
    units = StringField()


class Medication(EmbeddedDocument):
    name = StringField()
    dose = FloatField()
    units = StringField()


class BloodPressure(EmbeddedDocument):
    date = DateTimeField()
    reading = StringField()


class MedicalHistory(EmbeddedDocument):
    date = DateField()
    condition = StringField()


class Patient(Document):
    patient_id = StringField(required=True)
    name = StringField()
    case_pair = StringField()
    age = IntField()
    sex = StringField(max_length=1)
    presenting_complaint = StringField()
    examination = StringField()
    conclusion = StringField()
    heart_rate = IntField()
    blood_pressure = EmbeddedDocumentListField(BloodPressure)
    pathology = EmbeddedDocumentListField(PathologyResults)
    medication = EmbeddedDocumentListField(Medication)
    history = EmbeddedDocumentListField(MedicalHistory)
