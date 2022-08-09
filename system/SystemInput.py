import os 

def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função de input tratado - entra em loop e apenas para quando um digito aceitavel é digitado
    # typ - recebe o tipo de dado que o input deve receber 
    # message - A mensagem que vai dentro do input (que aparece antes do campo de digitação)
    # beforemessage - (opcional) Mensagem que aparece na linha de cima do input
        # Pode receber um valor em string ou uma lista de valores em string (são printados um abaixo do outro antes do input)
        # Pode receber, dentro da lista, uma lista com o primeiro parâmetro sendo uma chamada de função e o segundo o seu parâmetro
    # limit - (opcional) recebe uma lista com os valores minimo e máximo que o input aceite
    # consoleclear (opcional) - caso receba True, o console será limpo após cada tentativa errada de input
    # beforeinputclear (opcional) - caso receba True, o console será limpo antes do input 
    # end (opcional) - caso receba True, se o valor digitado for -1 o input é cancelado 

# input: 
    # tipo
    # mensagem do input

# mensagens 
    # cabeçalho
    # mensagem pré input 
    # (pode receber str e funções)

    # erro de tipo (digito errado)
    # erro de limite 

# props 
    # limpar console antes de aparecer o input 
    # limpar console após erro 
    # encerrar input (digitar -1)

# Função de input tratado - entra em loop e apenas para quando um digito aceitavel é digitado
    # dataType - recebe o tipo de dado a ser retornado pelo input 
    # inputMessage - recebe a mensagem que vai dentro do input 
    # beforeInputMessage - recebe o que é imprimido antes do input 
        # pode receber apenas uma string ou uma lista de elementos 
        # pode receber funções (passadas dentro de uma lista, com o primeiro item sendo a função e o segundo os parâmetros que ela recebe) - aceita até 3 parâmetros 
    # typeErrorMessage - recebe a mensagem de erro de tipo na digitação
    # limit - recebe uma lista com o maior e menor valores permitidos 
    # limitErrorMessage - recebe a mensagem de erro de limite (digito fora do limite estabelecido)
    # clearConsoleBeforeInput - se True, o console será limpo antes do input (fica apenas o cabeçalho e o input)
    # clearConsoleAfterError - se True, após qualquer erro o console será limpo e o input será refeito com o erro correspondente após o cabeçalho
    # digitBreak - caso seja digitado -1, o laço do input é quebrado. 
def system_input(dataType:type, #
        inputMessage:str = '', #
        beforeInputMessage:str or list="", #
        typeErrorMessage:str="O caractere digitado não é válido", #
        limit:list=[], #
        limitErrorMessage:str="O numero digitado não corresponde a uma opção.", #
        clearConsoleBeforeInput:bool=True, #
        clearConsoleAfterError:bool=True, #
        digitBreak:bool=False): #
    
    typerror = False
    limiterror = False

    while True:
        #----------- clear console before input     
        if clearConsoleBeforeInput:
            console_clear()

        # ---------- before message ----------
        if beforeInputMessage != "":
            if type(beforeInputMessage) == list:
                for message in beforeInputMessage:
                    if type(message) == list:
                        if len(message) == 1:
                            message[0]()
                        elif len(message) == 2:
                            if len(message[1]) == 1:
                                message[0](message[1][0])
                            if len(message[1]) == 2:
                                message[0](message[1][0], message[1][1])
                            if len(message[1]) == 3:
                                message[0](message[1][0], message[1][1], message[1][2])
                    else:
                        print(message)
            else:
                print(beforeInputMessage)

        # ---------- Print de erros ------------ 
        if typerror:
            print()
            print(typeErrorMessage)
            typerror = False
        if limiterror:
            print()
            print(limitErrorMessage)
            limiterror = False

        # ---------- Input ---------------------
        try:
            print()
            value = dataType(input(inputMessage))

            # ---------- Digit break ------------
            if digitBreak and (value == "-1" or value == -1):
                return -1

        except:
            typerror = True
            #----------- clear console after error
            if clearConsoleAfterError:
                console_clear()
            continue
        
        if limit == []:
            return value
        else:
            if value >= limit[0] and value <= limit[1]:
                return value 
            else:
                limiterror = True
                if clearConsoleAfterError:
                    console_clear()
                continue
        # ---------- tratamento de erros -------

