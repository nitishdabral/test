import pymongo
import urllib
client = pymongo.MongoClient("mongodb+srv://nitish:"+urllib.parse.quote('Nitish@123')+"@cluster0.oqqzj85.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
