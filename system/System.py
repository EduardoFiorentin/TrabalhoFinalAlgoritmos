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
                print(new_product)
                input()
                # self.database.add_new_product(new_product)

            # Mostrar produto por id 
            elif option == 2:
                SystemPrinter.menu_find_product_by_id()
                while True:
                    identification = input_value(int, "ID: ")
                    if identification == -1: break
                    SystemPrinter.menu_find_product_by_id()
                    DataPrinter.products_by_ID(identification)

            # Atualizar produto 


            # Relatorio de produto 
            elif option == 4:
                SystemPrinter.menu_products_report()
                while True:
                    choose = input_value(int, "Escolha um tipo: ")
                    if choose == -1: break

                    SystemPrinter.menu_products_report()

                    if choose == 0: DataPrinter.all_products()
                    elif choose == 1: DataPrinter.products_by_type(2)
                    elif choose == 2: DataPrinter.products_by_type(1)
                    elif choose == 3: DataPrinter.products_by_type(3)
                    elif choose == 4: DataPrinter.products_by_avaliability(True)
                    elif choose == 5: DataPrinter.products_by_avaliability(False)
                    else: ErrorPrinter.invalid_value()


            # Registrar compra 
                # TELA: LogIn do cliente 
                # TELA: Adição dos produtos 
                # TELA: Cupom fiscal 

            # Relatorio de compra 

            
            console_clear()
            SystemPrinter.menu_header()



