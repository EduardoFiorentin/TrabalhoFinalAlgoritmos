class WarningPrinter:

    # Avisos pra DataPrinter
    @staticmethod 
    def no_products_in_system():
        print("Não há produtos cadastrados no sistema!")

    @staticmethod 
    def no_products_with_this_type():
        print("Não há produtos deste tipo cadastrados no sistema!")

    @staticmethod 
    def no_products_avaliables():
        print("Não há produtos disponiveis no sistema!")

    @staticmethod 
    def no_products_unvaliables():
        print("Não há produtos indisponiveis no sistema!")
