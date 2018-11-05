import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["teste_pymongo"]
mycol = mydb["Clientes"]

###listar todas as bases
#print(myclient.list_database_names())

###listar base com nome hugo e informa que ela existe
# dblist = myclient.list_database_names()
# if "hugo" in dblist:
#   print("The database exists.")

###inserir informacoes
mydict = { "nome": "Tatu", "end": "Lago Amarelo" }
x = mycol.insert_one(mydict)

###listar nome collection
#print(mydb.list_collection_names())

###inserir informacoes com id especifica
#mydict = { "_id": 1, "nome": "Jacare", "end": "Lago Azul" }
#x = mycol.insert_one(mydict)

###inserir varios
# mylist = [
#   { "_id": 2, "nome": "Peter", "end": "Lowstreet 27"},
#   { "_id": 3, "nome": "Amy", "end": "Apple st 652"},
#   { "_id": 4, "nome": "Hannah", "end": "Mountain 21"},
#   { "_id": 5, "nome": "Michael", "end": "Valley 345"},
#   { "_id": 6, "nome": "Sandy", "end": "Ocean blvd 2"},
#   { "_id": 7, "nome": "Betty", "end": "Green Grass 1"},
#   { "_id": 8, "nome": "Richard", "end": "Sky st 331"}
# ]
# x = mycol.insert_many(mylist)