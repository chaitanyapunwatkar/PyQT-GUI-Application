import pprint
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)

mydatabase = client['Inspection']
mycollection = mydatabase['Company1']

record = {
    'sku_id': 'Item1',
    'unit_id': 4,
    'status': 'Good'
}

rec = mycollection.insert_one(record)
#mycollection.create_index([("sku_id",1), ("unit_id",-1)])

pprint.pprint(mycollection.index_information())

#mycollection.drop_indexes()
#pprint.pprint(mycollection.index_information())
