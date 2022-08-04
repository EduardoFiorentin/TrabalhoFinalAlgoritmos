import os
from DataPrinter import DataPrinter

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class SystemPrinter: 
    @staticmethod
    def menu_header_start():
        console_clear()
        print("-----------| BEM VINDO |-----------")
        print("Sistema de gerenciamento de compras")
        print("-----------------------------------")
        
    def menu_header():
        console_clear()
        print("-----------------------------------")
        print("Sistema de gerenciamento de compras")
        print("-----------------------------------")

    def menu_main_options():
        print()
        print("Escolha uma das opções para continuar:")
        print("[1] Cadastrar novo produto")
        print("[2] Consultar produto por código")
        print("[3] Atualizar produto")
        print("[4] Relatorio de produtos")
        print("[5] Registrar compra")
        print("[6] Relatorio de compras")
        print("[-1] Finalizar Programa")
        print()

    def menu_product_registration():
        console_clear()
        print("-----------------------------------")
        print("       Cadastro de Produtos        ")
        print("-----------------------------------")
        print()

    def menu_find_product_by_id(): 
        console_clear()
        print("-----------------------------------")
        print("    Consulta de Produtos por ID    ")
        print("-----------------------------------")
        print("[ID] - Consultar produto\n[-1] - Voltar")
        print()

    def menu_products_report(): 
        console_clear()
        print("-----------------------------------")
        print("       Relatorio de produtos       ")
        print("-----------------------------------")
        print("[0] - Todos os produtos")
        print("[1] - Filmes")
        print("[2] - Series")
        print("[3] - Documentarios")
        print("[4] - Disponíveis")
        print("[5] - Indisponíveis")
        print("[-1] - Sair")
        print()

    #TELA DO CLIENTE:
    #Login:
    def client_menu_login():
        print("-----------------------------------")
        print("           Área do Cliente         ")
        print("-----------------------------------")
        print('Faça seu Login para ter acesso à compras')
        # Função de cadastro...
    #Carrinho:
    def client_menu_shopping():
        print('''Login efetuado. Selecione o produto que você deseja comprar
        Obs. : você pode procurar por nome''')
    #Compras (Nota fiscal):
    def client_menu_receipt():
        print('''Suas compras foram realizadas com sucesso!
        Aqui está um resumo:''')
        # Exibe uma tabela, vai precisar de uma função


    #ATUALIZAÇÃO DE PRODUTOS 
    def menu_start_update_products(display=True):
        if display:
            console_clear()
            print("-----------------------------------")
            print("     Atualização de produtos       ")
            print("-----------------------------------")
        else:
            return "-----------------------------------\n     Atualização de produtos       \n-----------------------------------\n"

    def menu_update_product(database):
        print("Produtos:")
        DataPrinter.all_products(database)
        print()
        
        
        