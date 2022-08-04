from ErrorPrinter import ErrorPrinter
from SystemPrinter import console_clear

# Função de input tratado - entra em loop e apenas para quando um digito aceitavel é digitado
    # typ - recebe o tipo de dado que o input deve receber 
    # message - A mensagem que vai dentro do input (que aparece antes do campo de digitação)
    # beforemessage - (opcional) Mensagem que aparece na linha de cima do input
    # limit - (opcional) recebe uma lista com os valores minimo e máximo que o input aceite
    # consoleclear (opcional) - caso receba True, o console será limpo após cada tentativa errada de input
    # beforeinputclear (opcional) - caso receba True, o console será limpo antes do input 

def input_value(typ:type, message:str, beforemessage=False, limit:list=[], consoleclear=False, beforeinputclear=False):
    while True: 
        try: 
            if beforeinputclear:
                console_clear()

            # if beforemessage != False:
            #     print(beforemessage)

            if beforemessage != False:
                if type(beforemessage) == list:
                    for item in beforemessage: 
                        if type(item) == str:
                            print(item)
                        else: 
                            item() 
                else: 
                    print(beforemessage)


            value = typ(input(message))
            if limit != []:
                if value >= limit[0] and value <= limit[1]:
                    return value 
                else:
                    if consoleclear:
                        console_clear()
                        ErrorPrinter.invalid_value()
                    continue
            else:
                return value 
        except:
            if consoleclear:
                console_clear()
            ErrorPrinter.invalid_value()
            continue

# input_value(int, "Digite um número: ")