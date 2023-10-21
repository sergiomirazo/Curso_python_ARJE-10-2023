"""
    _summary_:
        This file contains the error handling for the application.
"""

lista = []

while True:
    entrada = input("Ingrese un número [q para salir] : ")
    if entrada == "q":
        break
    else:
        try:
            entrada = int(entrada)
            lista.append(entrada)
        except ValueError:
            print("Ingrese un número válido")
            
print(lista)