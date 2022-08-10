class ErrorPrinter:
    # Erros pra DataPrinter 
    @staticmethod 
    def product_not_exists():
        print("Produto não encontrado! Tente novamente.")
        print()

    # Erros pra SystemInput
    def invalid_value():
        print("Digito inválido. Tente novamente")
        print()

    def client_not_exists():
        print('Cliente não encontrado. Insira o login novamente...')
        print("[-1] - Sair")
        print()