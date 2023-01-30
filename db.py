import pymongo 

mongoURI = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongoURI)

db = client["ARTIFICIAL_INTELLIGENCE"]
collection = db['students'] # we can reference the database with these collections 

#create the database function 
def create(data) :
    data = dict(data)
    response = collection.insert_one(data)
    return str(response.inserted_id)

# finds the data from the collection from the data id 
def all():
    response = collection.find({})
    data = []
    for i in response:
        i['_id'] = str(i['_id'])
        data.append(i)
    return data

def get_one(condition ):
    response = collection.find_one({"name":condition})
    response['_id'] = str(response['_id'])
    return response

def update(name, data):
    response = collection.update_one({"name":name}, {"$set":data})
    return response.modified_count 

def delete(name):
    response = collection.delete_one({"name": name})
    return response.deleted_count 

