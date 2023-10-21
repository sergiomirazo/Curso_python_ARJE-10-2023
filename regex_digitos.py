import re
respuestas = ['Es 1000 g/L',
              '1000',
              '1',
              '233 que no??',
              'Ayyy no se',
              'hmmm yo creo que es 777',
              '1000 kg/m3'
              ]


numeros = ["".join(re.findall('\d', s)) for s in respuestas]
numeros.remove('')
data = []
print(numeros)
for x in numeros:
    x = float(x)
    data.append(x)

for x in data:
    if x==1000.0 or x==997.0 or x==1.0 or x==0.977:
        print("Correcto")
    else:
        print("Incorrecto")

