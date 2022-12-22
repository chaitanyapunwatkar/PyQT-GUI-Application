import pprint
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)

mydatabase = client['Inspection']
mycollection = mydatabase['Company1']

for i in range(1,101):
    if i%10 == 9:
        record = {
            'sku_id': 'Item1',
            'unit_id': i,
            'status': 'Bad'
        }
        rec = mycollection.insert_one(record)
        
    else:
        record = {
            'sku_id': 'Item1',
            'unit_id': i,
            'status': 'Good'
        }
        rec = mycollection.insert_one(record)
count = 0
#col = mycollection.find({}, )
#pprint.pprint(mycollection.index_information())
for row in mycollection.find():
    print(row) 
    count+=1
print(count)

#mycollection.drop()