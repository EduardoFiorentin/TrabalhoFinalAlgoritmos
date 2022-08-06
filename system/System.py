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
                Product.update(self.database)
                    

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



