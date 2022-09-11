import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["med_data"]

my_collection = db['patinet_data']


patient_record = {
    "Hospital number": "3432543",
    "Name": "Karen Baker",
    "Age": 45,
    "Sex": "F",
    "Blood pressure": [{"sys": 126}, {"dia": 72}],
    "Heart rate": 78,
    "Test results": [
        {
            "ECG": "\scans\ECGs\ecg00023.png"
        },
        {
            "BIOCHEM": [{"AST": 37}, {"CK": 180}, {"TROPT": 0.03}]
        }
    ]
}


my_collection.insert_one(patient_record)


for item in my_collection.find():
    print(item)
