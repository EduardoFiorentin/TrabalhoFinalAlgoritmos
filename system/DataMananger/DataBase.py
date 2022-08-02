import json
import sys
from termcolor import colored, cprint
import os

class DataBase: 
    def __init__(self):
        self.data = {}
        self.read_data_base()

    #ler base de dados e mandar pra self.database 
    def read_data_base(self):
        with open("database.json") as database:
            data = json.load(database)
        self.data = json.loads(data)
        

    #mandar os dados novos pro self.database 
    def update(self, data:dict()):
        for key, value in self.data.items(): 
            for newkey, newvalue in data.items(): 
                if newkey == key and newkey != "id":
                    self.data[key] = newvalue

    #manda o self.database pro database 
    def originUpdate(self):
        with open("database.json", 'w') as database:
            json.dump(json.dumps(self.data), database)

    #adicionar um novo produto na base de dados 
    def add_new_product(self, newProduct:dict()): 
        self.data["products"].append(newProduct)
        self.originUpdate()

    #modificar base de dados manualmente  
    def manual_data_base_update(self, newDataBase:dict()):
        with open("database.json", 'w') as database:
            json.dump(json.dumps(newDataBase), database)


# database = DataBase()
# database.add_new_product()














# ----------------------------------------------------------------

# ALTERAÇÕES MANUAIS NA BASE DE DADOS 
dicionario = {
    "products": [
        {
            "id": 1234,
            "productName":"Cachorra tetuda - O filme",
            "type": 1, 
            "price": 159000.99,
            "avaliable": True
        },
        {
            "id": 2345,
            "productName":"De quatro no convento",
            "type": 2, 
            "price": 19.95,
            "avaliable": True
        },
        {
            "id": 3456,
            "productName": "1001 noites sem beecrowd",
            "type": 3, 
            "price": 19.90,
            "avaliable": True
        }
    ],
    "users": [
        {
            "name": "Admin",
            "login": "AdminLog",
            "products": []
        }
    ],
    "purchaseHistory": [
        {
            "productID": 1234,
            "user": "Admin", 
            "productName": "ProductTest",
            "date": "data de compra"
        }
    ]
}

# database = DataBase()
# database.manual_data_base_update(dicionario)


# -------------------------------------------------------------------------------------


# DataBase.update()
# data.originUpdate()

# class Errors: 
#     @staticmethod  #colocar esta chave antes de cada método
#     def find_user_error(): #não colocar o self dentro do parenteses 
#         cprint("Usuário não encontrado! Verifique o ID e tente novamente!", "red")

# os.system('cls')
# Errors.find_user_error()