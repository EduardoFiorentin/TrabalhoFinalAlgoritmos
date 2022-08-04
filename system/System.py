from DataPrinter import DataPrinter
from SystemInputs import input_value
from SystemPrinter import SystemPrinter, console_clear
from DataBase import DataBase
from Products import Product
from ErrorPrinter import ErrorPrinter

class System: 
    def __init__(self):
        self.database = DataBase()
    
    def start(self):
        
        SystemPrinter.menu_header_start()

        while (True):

            SystemPrinter.menu_main_options()
            option = input_value(int, "Opção: ")

            # Fechar o sistema 
            if option == -1: break

            # Cadastrar novo produto
            elif option == 1:
                SystemPrinter.menu_product_registration()
                # new_product = input()
                new_product = Product.new_product()
                self.database.add_new_product(new_product)

            # Mostrar produto por id 
            elif option == 2:
                SystemPrinter.menu_find_product_by_id()
                while True:
                    identification = input_value(int, "ID: ")
                    if identification == -1: break
                    SystemPrinter.menu_find_product_by_id()
                    DataPrinter.products_by_ID(self.database, identification)

            # Atualizar produto 
            elif option == 3:
                while True:
                    changes = {}
                    SystemPrinter.menu_start_update_products()
                    SystemPrinter.menu_update_product(self.database)
                    id = input_value(int, "ID: ", beforemessage="Digite o ID do produto a ser modificado:\n[-1] - Sair")

                    if id == -1 : break

                    if self.database.id_exists(id):
                        while True: 
                            console_clear()

                            SystemPrinter.menu_start_update_products()
                            DataPrinter.products_by_ID(self.database, id)
                            

                            param = input_value(int, "Qual valor deseja modificar: ", beforemessage="[1] - Nome\n[2] - Tipo\n[3] - Preço\n[4] - Disponibilidade\n[-1] - Salvar e sair\n", consoleclear=True)

                            if param == -1: break

                            if param == 1: changes["productName"] = input_value(str, "Novo nome: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(self.database, id, print=False),""], beforeinputclear=True)

                            if param == 2: changes["type"] = input_value(int, "Novo tipo: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(self.database, id, print=False), "\n[1] - Série\n[2] - Filme\n[3] - Documentario", ""], limit=[1,3], consoleclear=True, beforeinputclear=True)

                            if param == 3: changes["price"] = input_value(float, "Novo preço: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(self.database, id, print=False), ""], beforeinputclear=True)

                            if param == 4: changes["avaliable"] = True if input_value(int, "Disponivel: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(self.database, id, print=False),"[1] - Disponível\n[2] - Indisponível", ""], limit=[1,2], consoleclear=True, beforeinputclear=True) == 1 else False

                    else:
                        console_clear()
                        print("Produto não existe")
                        continue
                    
                    print(changes)
                    input()

            # Relatorio de produto 
            elif option == 4:
                SystemPrinter.menu_products_report()
                while True:
                    choose = input_value(int, "Escolha um tipo: ")
                    if choose == -1: break

                    SystemPrinter.menu_products_report()

                    if choose == 0: DataPrinter.all_products(self.database)
                    elif choose == 1: DataPrinter.products_by_type(self.database, 2)
                    elif choose == 2: DataPrinter.products_by_type(self.database, 1)
                    elif choose == 3: DataPrinter.products_by_type(self.database, 3)
                    elif choose == 4: DataPrinter.products_by_avaliability(self.database, True)
                    elif choose == 5: DataPrinter.products_by_avaliability(self.database, False)
                    else: ErrorPrinter.invalid_value()


            # Registrar compra 
                # TELA: LogIn do cliente 
                # TELA: Adição dos produtos 
                # TELA: Cupom fiscal 

            # Relatorio de compra 

            
            console_clear()
            SystemPrinter.menu_header()



