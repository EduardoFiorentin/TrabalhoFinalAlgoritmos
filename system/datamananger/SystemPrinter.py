import os

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
