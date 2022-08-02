from ErrorPrinter import ErrorPrinter

def input_value(type:type, message:str):
    try: 
        value = type(input(message))
        return value 
    except:
        ErrorPrinter.invalid_value()
        input_value(type, message)

# input_value(int, "Digite um número: ")