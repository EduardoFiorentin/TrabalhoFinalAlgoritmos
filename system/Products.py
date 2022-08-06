import uuid
from SystemPrinter import console_clear, SystemPrinter
from DataPrinter import DataPrinter
from SystemInputs import input_value
from SystemPrinter import SystemPrinter, console_clear

class Product: 
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
    

    def update(database):
        while True:
                    changes = {}
                    SystemPrinter.menu_start_update_products()
                    id = input_value(int, "ID: ", beforemessage=[[SystemPrinter.menu_update_product, database], "Digite o ID do produto a ser modificado:\n[-1] - Sair"], consoleclear=True)

                    if id == -1 : break

                    if database.id_exists(id):
                        while True: 
                            console_clear()

                            SystemPrinter.menu_start_update_products()
                            DataPrinter.products_by_ID(database, id)
                            
                            param = input_value(int, "Qual valor deseja modificar: ", beforemessage="[1] - Nome\n[2] - Tipo\n[3] - Preço\n[4] - Disponibilidade\n[-1] - Salvar e sair\n[-2] - Sair sem salvar\n", consoleclear=True)

                            if param == -1 or param == -2: break

                            if param == 1: changes["productName"] = input_value(str, "Novo nome: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(database, id, print=False),""], beforeinputclear=True)

                            if param == 2: changes["type"] = input_value(int, "Novo tipo: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(database, id, print=False), "\n[1] - Série\n[2] - Filme\n[3] - Documentario", ""], limit=[1,3], consoleclear=True, beforeinputclear=True)

                            if param == 3: changes["price"] = input_value(float, "Novo preço: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(database, id, print=False), ""], beforeinputclear=True)

                            if param == 4: changes["avaliable"] = True if input_value(int, "Disponivel: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(database, id, print=False),"[1] - Disponível\n[2] - Indisponível", ""], limit=[1,2], consoleclear=True, beforeinputclear=True) == 1 else False
                    else:
                        console_clear()
                        continue

                    if param == -1:
                        database.productUpdate(id, changes)

# Gerar id : int(str(uuid.uuid1().int)[:6])
# Product.new_product()