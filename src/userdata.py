# importing MongoClient 
from pymongo import MongoClient

# Configuring and Connecting database
client = MongoClient('mongodb://127.0.0.1:27017')

#if there is no databse named cryptocurrency, mongoDB ll automatically create one
db = client['cryptocurrency']
coin = db.coins

coin_1 = {'coinname' : 'bitcoin',
       'price': 500,
       'Algo': 'POW'
       }
coin_2 = {'coinname' : 'ether',
       'price': 200,
       'Algo': 'POS'
       }
coin_3 = {'coinname' : 'ripple',
       'price': 0.25,
       'Algo': 'RPCA'
       }

#inserting data if only one data is there we can use insert_one instead insert_many.
result = coin.insert_many([coin_1,coin_2,coin_3])
print(result)
