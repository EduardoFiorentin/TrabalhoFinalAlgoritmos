import uuid
from SystemPrinter import console_clear, SystemPrinter
from DataPrinter import DataPrinter
from SystemInputs import input_value
from SystemPrinter import SystemPrinter, console_clear

class Product: 

    # GERAR NOVO PRODUTO (opção 1)
    @staticmethod 
    def new_product():
        productname = input_value(str, "Nome do produto: ")

        console_clear()
        SystemPrinter.menu_product_registration()
        typ = input_value(int, "Tipo: ", beforemessage=f"Tipos:\n[1] - Serie\n[2] - Filme\n[3] - Documentário", limit=[1,3], consoleclear=True)

        console_clear()
        SystemPrinter.menu_product_registration()
        price = input_value(float, "Preço: ", consoleclear=True)

        console_clear()
        SystemPrinter.menu_product_registration()
        avaliable = True if input_value(int,"\nDisponível: ", "[1] - Disponível\n[2] - Indisponível", limit=[1,2], consoleclear=True) == 1 else False

        console_clear()

        new_product =  {
        "id": int(str(uuid.uuid1().int)[:6]),
        "productName" : productname,
        "type": typ, 
        "price":  price,
        "avaliable": avaliable
        }

        return new_product
    
