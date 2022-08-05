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
    
    def productUpdate(self, id:int, data:dict()):
        for item in self.data["products"]:
            if item["id"] == id:
                for key, value in item.items():
                    for newkey, newvalue in data.items():
                        if key != "id" and key == newkey:
                            item[key] = newvalue
            
        self.originUpdate()

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

    # Verifica se um id existe na base de dados 
    def id_exists(self, id):
        for item in self.data["products"]:
            if item["id"] == id:
                return True
        return False
















# ----------------------------------------------------------------

# ALTERAÇÕES MANUAIS NA BASE DE DADOS 
dicionario = {
    "products": [
        {
            "id": 123456,
            "productName":"Cachorra tetuda - O filme",
            "type": 2, 
            "price": 159000.99,
            "avaliable": True
        },
        {
            "id": 234512,
            "productName":"De quatro no convento",
            "type": 2, 
            "price": 19.95,
            "avaliable": True
        },
        {
            "id": 345665,
            "productName": "1001 noites sem beecrowd",
            "type": 3, 
            "price": 19.90,
            "avaliable": True
        },
        {
            "id": 654324,
            "productName": "Como treinar seu dragão",
            "type": 2, 
            "price": 199.99,
            "avaliable": False
        },
        {
            "id": 936594,
            "productName": "Cartas para Julieta",
            "type": 2, 
            "price": 49.90,
            "avaliable": True
        },
        {
            "id": 724963,
            "productName": "Stranger Things",
            "type": 1, 
            "price": 19.90,
            "avaliable": True
        }, 
        {
            "id": 912478,
            "productName": "Professor Polvo",
            "type": 3, 
            "price": 0,
            "avaliable": True
        },
        {
            "id": 825483,
            "productName": "The good place",
            "type": 1, 
            "price": 59.90,
            "avaliable": True
        },
        {
            "id": 528439,
            "productName": "O que fazemos nas sombras",
            "type": 2, 
            "price": 100,
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