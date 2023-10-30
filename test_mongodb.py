from pymongo import MongoClient

client = MongoClient("mongodb+srv://new-user1:1234@cluster0.cocbi8g.mongodb.net/?retryWrites=true&w=majority")

#create schema
db = client.test

#create document
list = db.mydata

list.insert_one({
    "data" : "test",
    "name" : "UB"
})
