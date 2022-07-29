# Importar o módulo
import json

# # String em formato JSON
# data_JSON =  """
# {
# 	"size": "Medium",
# 	"price": 15.67,
# 	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
# 	"client": {
# 		"name": "Jane Doe",
# 		"phone": "455-344-234",
# 		"email": "janedoe@email.com"
# 	}
# }
# """

# # Converter a string em JSON em um dicionário
# data_dict = json.loads(data_JSON)

# print(data_dict)


# Dicionário em Python
# client = {
#     "name": "Nora",
#     "age": 56,
#     "id": "45355",
#     "eye_color": "green",
#     "wears_glasses": False
# }

# # Obter uma string formatada em JSON
# client_JSON = json.dumps(client)

# with open("db.json", 'w') as database:
#     json.dump(client_JSON, database)

with open("db.json") as file:
    # Carregar seu conteúdo e torná-lo um novo dicionário
    data = json.load(file)

data_dict = json.loads(data)

print(data_dict["name"])