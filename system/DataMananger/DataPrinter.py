import pandas as pd 
from DataBase import DataBase
from ErrorPrinter import ErrorPrinter
from WarningPrinter import WarningPrinter
# Converte a lista de dicionarios recebidos da base de dados em uma lista de listas (requisito para o tabulação do pandas)
    # a função também funciona com filtros - filter é o tipo de filtro (por id, nome, etc), e a keyFilter é o nome do filtro em sí (o id que se quer, o nome que se quer, etc)
def convert_dict_to_list(dictionare:list(dict()), filter=None, keyFilter=None):
    dictlist = []
    for item in dictionare:
        locallist = []
        for key, value in item.items():

            if key == "avaliable" and value == True: 
                value = "Sim"
            elif key == "avaliable" and value == False:
                value = "Não"

            locallist.append(value)

        # aplicação de filtros
        if filter == None:
            dictlist.append(locallist)
        elif filter == "ID":
            if item['id'] == keyFilter:
                dictlist.append(locallist)
        elif filter == "type":
            if item['type'] == keyFilter:
                dictlist.append(locallist)
        elif filter == "avaliable":
            if item['avaliable'] == keyFilter:
                dictlist.append(locallist)

    return dictlist

# Imprime a tabela de itens
def printdataframe(allproductslist:list(list())):
    dataframe = pd.DataFrame(allproductslist, columns = ["ID", "Nome do produto", "Tipo", "Preço", "Disponivel"])
    print(dataframe)


class DataPrinter: 

    # IMPRIMIR TODOS OS PRODUTOS
    @staticmethod
    def all_products():
        allproductsdict = DataBase().data["products"]
        allproductslist = convert_dict_to_list(allproductsdict)
        if allproductslist == []:
            WarningPrinter.no_products_in_system()
        else:
            printdataframe(allproductslist)

    # CONSULTA DE PRODUTOS POR ID
    @staticmethod 
    def products_by_ID(id:int):
        allproductsdict = DataBase().data["products"]
        allproductslist = convert_dict_to_list(allproductsdict, "ID", id)
        if allproductslist == []:
            ErrorPrinter.product_not_exists()
        else:
            printdataframe(allproductslist)

    # CONSULTA DE PRODUTOS POR TIPO
    @staticmethod 
    def products_by_type(type:int):
        allproductsdict = DataBase().data["products"]
        allproductslist = convert_dict_to_list(allproductsdict, "type", type)
        if allproductslist == []:
            WarningPrinter.no_products_with_this_type()
        else:
            printdataframe(allproductslist)

    # CONSULTA DE PRODUTOS POR DISPONIBILIDADE
    @staticmethod
    def products_by_avaliability(avaliability:bool=True):
        allproductsdict = DataBase().data["products"]
        allproductslist = convert_dict_to_list(allproductsdict, "avaliable", avaliability)
        if allproductslist == []:
            if avaliability == True:
                WarningPrinter.no_products_avaliables()
            else:
                WarningPrinter.no_products_unvaliables()
        else:
            printdataframe(allproductslist)

# DataPrinter.products_by_ID(12345)