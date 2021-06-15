import pymongo

class MongoPythonDBController:
    def __init__(self, host, dbname):
        self.host = host
        self.dbname = dbname

    def insertDetection(self, document):
        client = pymongo.MongoClient(self.host)
        db = client[self.dbname]
        # Insert document in collection detections
        detections = db["detections"]
        newRecord = detections.insert_one(document)