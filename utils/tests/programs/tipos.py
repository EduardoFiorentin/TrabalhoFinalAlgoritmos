def printer(message):
    print(message)


lista = [printer, 'b']

# if type(lista) == list:
#     for item in lista: 
#         if type(item) == str:
#             print(item)
#         elif type(item) : 
#             item() 

print(type(lista[0]("message")))