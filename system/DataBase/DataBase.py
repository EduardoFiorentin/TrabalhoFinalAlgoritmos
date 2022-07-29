import json
import sys
from termcolor import colored, cprint
import os

class DataBase: 
    def __init__(self):
        self.data = {}

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

    
# data = DataBase()
# data.read_data_base()
# print(data.data)
# dic = {"name": "mula", 'id': 'nao pode ser esse', 'age': 545}
# data.update(dic)
# data.originUpdate()


# DataBase.update()
# data.originUpdate()

class Errors: 
    @staticmethod  #colocar esta chave antes de cada método
    def find_user_error(): #não colocar o self dentro do parenteses 
        cprint("Usuário não encontrado! Verifique o ID e tente novamente!", "red")

os.system('cls')
Errors.find_user_error()