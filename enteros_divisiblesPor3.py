data = []

def ingresar(i):
    txt = input("Ingresa el número " + str(i) + " : ")
    return txt

try:
    n = int(input("Ingresa la cantidad de números que deseas ingresar : "))
except ValueError:
    print("Ingresa un número válido")

for i in range(1,n+1):
    try:
        entero = int(ingresar(i))
    except ValueError:
        print("Ingresa un número válido")
        entero = int(ingresar(i))
    if entero % 3 == 0:
        data.append(entero)

print(data)
