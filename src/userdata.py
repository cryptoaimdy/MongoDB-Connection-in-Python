from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client['cryptocurrency']
coins = db.coins

coin = {'Coinname' : 'bitcoin',
       'price': 500,
       'Algo': 'POW'
       }

result= coins.insert_one(coin)
print(result)