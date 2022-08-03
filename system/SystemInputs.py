from ErrorPrinter import ErrorPrinter

def input_value(typ:type, message:str, beforemessage=False, limit:list=[]):
    while True: 
        try: 
            if beforemessage != False:
                print(beforemessage)

            value = typ(input(message))
            if limit != []:
                if value >= limit[0] and value <= limit[1]:
                    return value 
                else:
                    # input_value(typ, message, beforemessage, limit)
                    continue
            else:
                return value 
        except:
            ErrorPrinter.invalid_value()
            # input_value(typ, message, beforemessage, limit)
            continue

# input_value(int, "Digite um número: ")