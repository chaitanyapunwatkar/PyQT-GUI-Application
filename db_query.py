from pymongo import MongoClient


class DbQueries():
    def __init__(self):
        client = MongoClient('localhost', 27017)
        mydatabase = client['Inspection']
        self.mycollection = mydatabase['Company1']
        
    def status_filter(self,status):
        unit_ids = []
        if status != "All":
            for row in self.mycollection.find({ "status": status}):
                unit_ids.append(row["unit_id"])
        else:
            for row in self.mycollection.find({}):
                unit_ids.append(row["unit_id"])
        return unit_ids
    
    def count(self):
        #self.mycollection.find().count()
        return self.mycollection.count_documents({})
    
    def id_status(self, unit_id):
        col = self.mycollection.find({"unit_id": unit_id})
        for i in  col:
            return i['status']
            


