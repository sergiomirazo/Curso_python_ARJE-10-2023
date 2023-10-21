n = 1
data = []

def ingresar():
    global n
    txt = input(f"Ingresa el intento numero "+ str(n)+ ":")
    return txt

print("Por favor, ingresa un palíndromo" +'\n' +
      'Si no ingresas un palíndromo...'+'\n'+
      '\n'+'PIERDES')

print('================================================')
while True:
    txt = ingresar()
    txt1 = list(txt)
    for x in txt1:
        if x ==' ':
            txt1.remove(x)
        else:
            pass
    
    txt2 = list(txt)
    txt2.reverse()
    if txt1 == txt2:
        print("Palíndromo detectado!")
        n += 1
        data.append(txt)
    
    else:
        if not data:
            print('No es palíndromo, PERDISTE')
        else:
            n -= 1
            print(f"Has ingresado {n} palíndromos")
            print(data)
        break
