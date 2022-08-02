from DataPrinter import DataPrinter
from SystemInputs import input_value
from DataBase import DataBase

class System: 
    def __init__(self):
        self.database = DataBase()
    
    def start(self):
        while (True):
            option = input_value(int, "Opção: ")
            if option == -1:
                break
            elif option == 2:
                identification = input_value(int, "ID: ")
                DataPrinter.products_by_ID(identification)