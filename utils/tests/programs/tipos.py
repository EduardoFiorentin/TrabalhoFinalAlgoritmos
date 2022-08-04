def printer():
    print("A lista foi")


lista = [printer, 'b']

if type(lista) == list:
    for item in lista: 
        if type(item) == str:
            print(item)
        else: 
            item() 