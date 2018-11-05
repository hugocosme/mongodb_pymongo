import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["teste_pymongo"]
mycol = mydb["Clientes"]

###buscando um
#x = mycol.find_one()
#print(x)

###buscando todos
#for x in mycol.find():
#    print(x)

#buscando um especifico
