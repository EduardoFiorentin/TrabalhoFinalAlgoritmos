import pandas as pd 
from DataBase import DataBase

def convert_dict_to_list(dictionare:list(dict())):
    dictlist = []
    for item in dictionare:
        locallist = []
        for key, value in item.items():

            if key == "avaliable" and value == True: 
                value = "Sim"
            elif key == "avaliable" and value == False:
                value = "Não"

            locallist.append(value)
        dictlist.append(locallist)
    return dictlist


class Printer: 
    @staticmethod
    def all_products():
        allproductsdict = DataBase().data["products"]
        allproductslist = convert_dict_to_list(allproductsdict)
        dataframe = pd.DataFrame(allproductslist, columns = ["ID", "Nome do produto", "Tipo", "Preço", "Disponivel"])
        print(dataframe)

Printer.all_products()
