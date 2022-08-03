import uuid
from SystemInputs import input_value
from SystemPrinter import console_clear

class Product: 
    @staticmethod 
    def new_product():
        productname = input_value(str, "Nome do produto: ")
        console_clear()
        typ = input_value(int, "Tipo: ", beforemessage="Tipos:\n[1] - Serie\n[2] - Filme\n[3] - Documentário", limit=[1,3])
        console_clear()
        price = input_value(float, "Preço: ")
        console_clear()
        avaliable = True if input_value(int, "Disponível: ", "[1] - Disponível\n[2] - Indisponível", limit=[1,2]) == 1 else False
        console_clear()

        new_product =  {
        "id": int(str(uuid.uuid1().int)[:6]),
        "productName" : productname,
        "type": typ, 
        "price":  price,
        "avaliable": avaliable
        }

        print(new_product)

# Gerar id : int(str(uuid.uuid1().int)[:6])
Product.new_product()