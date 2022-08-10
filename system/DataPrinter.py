import pandas as pd 
from DataBase import DataBase
from ErrorPrinter import ErrorPrinter
from WarningPrinter import WarningPrinter
from SystemPrinter import SystemPrinter

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

            if key == "type" and value == 1:
                value = "Série"
            elif key == "type" and value == 2:
                value = "Filme"
            elif key == "type" and value == 3:
                value = "Documentario"

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
    print()


class DataPrinter: 

    # IMPRIMIR TODOS OS PRODUTOS
    @staticmethod
    def all_products(database):
        allproductsdict = database.data["products"]
        allproductslist = convert_dict_to_list(allproductsdict)
        allproductslist = sorted(allproductslist, key=lambda product: product[1])
        if allproductslist == []:
            WarningPrinter.no_products_in_system()
        else:
            printdataframe(allproductslist)

    # CONSULTA DE PRODUTOS POR ID
        # print(opcional) - se receber False, retorna o item ao invés de printa-los diretamente
        # lst (opcioanal) - funciona apenas quando print=False - Se receber True, retorna os dados em lista ao invés de dataframe
    @staticmethod 
    def products_by_ID(database, id:int, print=True, lst=False):
        allproductsdict = database.data["products"]
        allproductslist = convert_dict_to_list(allproductsdict, "ID", id)
        if allproductslist == []:
            ErrorPrinter.product_not_exists()
        else:
            if print:
                printdataframe(allproductslist)
            else:
                if lst:
                    return allproductslist
                return pd.DataFrame(allproductslist, columns = ["ID", "Nome do produto", "Tipo", "Preço", "Disponivel"])

    # CONSULTA POR NOME 
    @staticmethod
    def products_by_name(database, type:str):
        allproductsdict = database.data["products"]
        allproductslist = convert_dict_to_list(allproductsdict, "name", type)
        if allproductslist == []:
            WarningPrinter.no_products_with_this_name()
        else:
            printdataframe(allproductslist)

    # CONSULTA DE PRODUTOS POR TIPO
    @staticmethod 
    def products_by_type(database, type:int):
        allproductsdict = database.data["products"]
        allproductslist = convert_dict_to_list(allproductsdict, "type", type)
        allproductslist = sorted(allproductslist, key=lambda product: product[1])
        if allproductslist == []:
            WarningPrinter.no_products_with_this_type()
        else:
            printdataframe(allproductslist)


    # CONSULTA DE PRODUTOS POR DISPONIBILIDADE
    @staticmethod
    def products_by_avaliability(database, avaliability:bool=True):
        allproductsdict = database.data["products"]
        allproductslist = convert_dict_to_list(allproductsdict, "avaliable", avaliability)
        allproductslist = sorted(allproductslist, key=lambda product: product[1])
        if allproductslist == []:
            if avaliability == True:
                WarningPrinter.no_products_avaliables()
            else:
                WarningPrinter.no_products_unvaliables()
        else:
            printdataframe(allproductslist)

    # GERA CUPOM FISCAL DE COMPRA
    def purchase_receipt(products): 
        table = pd.DataFrame(products, columns = ["Código", "Nome do produto", "Tipo", "Preço", "Data de compra"])
        print(table)


    # GERA O RELATÓRIO DE COMPRAS 
    def purchace_report(database):
        data = database.data["purchaseHistory"]
        data = convert_dict_to_list(data)
        if data == []:
            # SystemPrinter.menu_no_purchace_historic()
            print('sem produtos')
        else:
            table = pd.DataFrame(data, columns = ["Login", "Valor total", "Data da compra"])
            print(table)