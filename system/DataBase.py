import json
import sys
import os
import datetime

# CLASSE QUE CONTROLA A BASE DE DADOS 
class DataBase: 
    def __init__(self):
        self.data = {}
        self.read_data_base()

    # ler base de dados e mandar pra self.data 
    def read_data_base(self):
        with open("database.json") as database:
            data = json.load(database)
        self.data = json.loads(data)
        

    # mandar os dados novos pro self.data (usado pela opção 3)
    def update(self, data:dict()):
        for key, value in self.data.items(): 
            for newkey, newvalue in data.items(): 
                if newkey == key and newkey != "id":
                    self.data[key] = newvalue
    
    # Faz o update de um produto existente
    def productUpdate(self, id:int, data:dict()):
        for item in self.data["products"]:
            if item["id"] == id:
                for key, value in item.items():
                    for newkey, newvalue in data.items():
                        if key != "id" and key == newkey:
                            item[key] = newvalue
            
        self.originUpdate()

    # manda o self.database pro database 
    def originUpdate(self):
        with open("database.json", 'w') as database:
            json.dump(json.dumps(self.data), database)

    # adicionar um novo produto na base de dados 
    def add_new_product(self, newProduct:dict()): 
        self.data["products"].append(newProduct)
        self.originUpdate()

    # modificar base de dados manualmente (ausada apenas no desenvolvimento)
    def manual_data_base_update(self, newDataBase:dict()):
        with open("database.json", 'w') as database:
            json.dump(json.dumps(newDataBase), database)

    # Verifica se um produto com id passado existe na base de dados 
    def id_exists(self, id):
        for item in self.data["products"]:
            if item["id"] == id:
                return True
        return False

    # Verifica se um cliente existe na base de dados 
    def client_exists(self, client:str):
        for user in self.data["users"]:
            if user["login"] == client:
                return True
        return False

    # salva as compras no histórico do cliente
    def save_buying(self, client_login:str, products_list:list(), total_value:float):
        for user in self.data["users"]:
            if user["login"] == client_login:
                for product in products_list:
                    user["products"].append(product)

        # salvar as compras no histórico geral de compras 
        historic = {
            "login": client_login, 
            "total_value": total_value,
            "date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        self.data["purchaseHistory"].append(historic)

        self.originUpdate()

    


# ----------------------------------------------------------------

# ALTERAÇÕES MANUAIS NA BASE DE DADOS 
# dicionario = {
#     "products": [
#         {
#             "id": 123456,
#             "productName": "Como treinar seu dragão",
#             "type": 2, 
#             "price": 199.99,
#             "avaliable": False
#         },
#         {
#             "id": 789456,
#             "productName": "Cartas para Julieta",
#             "type": 2, 
#             "price": 49.90,
#             "avaliable": True
#         },
#         {
#             "id": 456789,
#             "productName": "Stranger Things",
#             "type": 1, 
#             "price": 19.90,
#             "avaliable": True
#         }, 
#         {
#             "id": 456123,
#             "productName": "Professor Polvo",
#             "type": 3, 
#             "price": 0,
#             "avaliable": True
#         },
#         {
#             "id": 825483,
#             "productName": "The good place",
#             "type": 1, 
#             "price": 59.90,
#             "avaliable": True
#         },
#         {
#             "id": 528439,
#             "productName": "O que fazemos nas sombras",
#             "type": 2, 
#             "price": 100,
#             "avaliable": True
#         }
#     ],
#     "users": [
#         {
#             "name": "Admin",
#             "login": "AdminLog",
#             "products": []
#         },
#         {
#             "name": "Judah",
#             "login": "judah123",
#             "products": []
#         },
#         {
#             "name": "Eduardo",
#             "login": "eduardo",
#             "products": []
#         },
#         {
#             "name": "Ana Paula Pereira",
#             "login": "anapaula",
#             "products": []
#         }
#     ],
#     "purchaseHistory": []
# }

# database = DataBase()
# database.manual_data_base_update(dicionario)
