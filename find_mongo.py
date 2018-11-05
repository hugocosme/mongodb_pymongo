#referencia https://www.w3schools.com/python/python_mongodb_find.asp
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["teste_pymongo"]
mycol = mydb["Clientes"]

###buscando o primeiro da collection Clientes
#x = mycol.find_one()
#print(x)

###buscando todos os documentos da collection Clientes
for x in mycol.find():
     print(x)

###buscando um especifico na collection Clientes
# for x in mycol.find({},{ "_id": 0, "nome": 1, "end": 1 }):
#   print(x)