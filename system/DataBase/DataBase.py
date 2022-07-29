import json

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
        self.data.update(data)

    #manda o self.database pro database 
    def originUpdate(self):
        with open("database.json", 'w') as database:
            json.dump(json.dumps(self.data), database)

    
data = DataBase()
dic = {"name": "mula"}
data.update(dic)
data.originUpdate()
data.originUpdate()