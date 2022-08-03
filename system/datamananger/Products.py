import uuid
from SystemInputs import input_value

# Fazer uma classe com um método estático new_product que possa ser chamado na hora de cadastrar um novo produto (opção 1 do código principal)

# Ao ser chamado, o método deve pedir nome, tipo, preço e se tá disponível para venda. 

# A estrutura a ser retorada deve ser a seguinte: 
# {
#     "id": 1234 (int),
#     "productName":"nome que vier no input" (string),
#     "type": tipo que vier no input (int), 
#     "price": 159000.99 (float),
#     "avaliable": True (boolean )
# }

# OBS: O id deve ser gerado pelo programa (pode ser um número aleatorio - deve ter 6 digitos)
# OBS: Os itens devem estar na ordem em que aparacem no exemplo acima pra não dar conflito na hora de imprimir os dados 

class Product: 
    @staticmethod 
    def new_product():
        productname = input_value(str, "Nome do produto: ")
        typ = input_value(int, "Tipo: ", beforemessage="Tipos:\n[1] - Serie\n[2] - Filme\n[3] - Documentário", limit=[1,3])
        price = input_value(float, "Preço: ")
        avaliable = True if input_value(int, "Disponível: ", "[1] - Disponível\n[2] - Indisponível", limit=[1,2]) == 1 else False

        new_product =  {
        "id": int(str(uuid.uuid1().int)[:6]),
        "productName" : productname,
        "type": typ, 
        "price":  price,
        "avaliable": avaliable
        }

        print(new_product)

# Gerar id : int(str(uuid.uuid1().int)[:6])
# Product.new_product()