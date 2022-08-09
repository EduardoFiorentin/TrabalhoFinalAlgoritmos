from DataPrinter import DataPrinter
from SystemInputs import input_value
from SystemPrinter import SystemPrinter, console_clear
from DataBase import DataBase
from Products import Product
from ErrorPrinter import ErrorPrinter
from WarningPrinter import WarningPrinter
from SystemInput import system_input
import datetime

class System: 
    def __init__(self):
        self.database = DataBase()
    
    def start(self):
        
        SystemPrinter.menu_header_start()

        while (True):

            SystemPrinter.menu_main_options()
            option = input_value(int, "Opção: ")
            # option = system_input(int, inputMessage="Opção: ",
            #  beforeInputMessage=[[SystemPrinter.menu_main_options]],
            #  )

            # Fechar o sistema 
            if option == -1: break

            # Cadastrar novo produto
            elif option == 1:
                SystemPrinter.menu_product_registration()
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
                    id = input_value(int, "ID: ", beforemessage=[[SystemPrinter.menu_update_product, self.database], "Digite o ID do produto a ser modificado:\n[-1] - Sair"], consoleclear=True)

                    if id == -1 : break

                    if self.database.id_exists(id):
                        while True: 
                            console_clear()

                            SystemPrinter.menu_start_update_products()
                            DataPrinter.products_by_ID(self.database, id)
                            
                            param = input_value(int, "Qual valor deseja modificar: ", beforemessage="[1] - Nome\n[2] - Tipo\n[3] - Preço\n[4] - Disponibilidade\n[-1] - Salvar e sair\n[-2] - Sair sem salvar\n", consoleclear=True)

                            if param == -1 or param == -2: break

                            if param == 1: changes["productName"] = input_value(str, "Novo nome: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(self.database, id, print=False),""], beforeinputclear=True)

                            if param == 2: changes["type"] = input_value(int, "Novo tipo: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(self.database, id, print=False), "\n[1] - Série\n[2] - Filme\n[3] - Documentario", ""], limit=[1,3], consoleclear=True, beforeinputclear=True)

                            if param == 3: changes["price"] = input_value(float, "Novo preço: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(self.database, id, print=False), ""], beforeinputclear=True)

                            if param == 4: changes["avaliable"] = True if input_value(int, "Disponivel: ", beforemessage=[SystemPrinter.menu_start_update_products(display=False), DataPrinter.products_by_ID(self.database, id, print=False),"[1] - Disponível\n[2] - Indisponível", ""], limit=[1,2], consoleclear=True, beforeinputclear=True) == 1 else False
                    else:
                        console_clear()
                        continue

                    if param == -1:
                        self.database.productUpdate(id, changes)
                    

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
            elif option == 5:
                # TELA: LogIn do cliente 
                console_clear()
                SystemPrinter.client_menu_header()
                SystemPrinter.client_menu_login()
                while True:
                    client_login = input_value(str, "Login do cliente: ")
                    if client_login == "-1": break

                    client_exists = self.database.client_exists(client_login)
                    # TELA: Adição dos produtos 
                    if client_exists:
                        products_list = []
                        total_value = 0
                        console_clear()
                        SystemPrinter.client_menu_header()
                        SystemPrinter.client_menu_shopping()

                        while True:
                            id = input_value(int, "ID do produto: ", beforemessage="[ID] - Adicionar produto\n[-1] -  Encerrar compra\n[-2] - Cancelar compra")
                            if id == -2: break
                            if id == -1:
                                self.database.save_buying(client_login, products_list, total_value)
                                # TELA: Cupom fiscal 
                                console_clear()
                                DataPrinter.purchase_receipt(products_list)
                                print(f"Total: {total_value}")
                                break

                            if self.database.id_exists(id):

                                product = DataPrinter.products_by_ID(self.database, id, print=False, lst=True)
                                product = product[0]
                                product[-1] = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
                                total_value += product[3]
                                products_list.append(product)

                                console_clear()
                                SystemPrinter.client_menu_header()
                                WarningPrinter.product_added()

                            else:
                                console_clear()
                                SystemPrinter.client_menu_header()
                                ErrorPrinter.product_not_exists()
                        
                    else:
                        console_clear()
                        SystemPrinter.client_menu_header()
                        ErrorPrinter.client_not_exists()

                    # break
                

            # Relatorio de compra 
            elif option == 6:
                console_clear()
                DataPrinter.purchace_report(self.database)
                input("Pressione enter para continuar:")
            
            console_clear()
            SystemPrinter.menu_header()



