from DataPrinter import DataPrinter
from SystemInputs import input_value
from DataBase import DataBase
from Products import Product

class System: 
    def __init__(self):
        self.database = DataBase()
    
    def start(self):
        while (True):
            option = input_value(int, "Opção: ")

            # Fechar o sistema 
            if option == -1:
                break

            # Cadastrar novo produto
            elif option == 1:
                new_product = Product.new_product()
                self.database.add_new_product(new_product)

            # Mostrar produto por id 
            elif option == 2:
                while True:
                    identification = input_value(int, "ID: ")
                    if identification == -1: break
                    DataPrinter.products_by_ID(identification)

            # Relatorio de produto 
            elif option == 3:
                while True:
                    choose = input_value(int, "Escolha um tipo: ")
                    if choose == -1: break
                    if choose == 0: DataPrinter.all_products()
                    if choose == 1: DataPrinter.products_by_type(2)
                    if choose == 2: DataPrinter.products_by_type(1)
                    if choose == 3: DataPrinter.products_by_type(3)
                    if choose == 4: DataPrinter.products_by_avaliability(True)
                    if choose == 5: DataPrinter.products_by_avaliability(False)


            # Registrar compra 


            # Relatorio de compra 

