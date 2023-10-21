import re

comandos = ['musica', 'luces', 'noticias', 'receta']
prompt = input("->")
data = []

for comando in comandos:
    coincidencia = re.findall(r'\b{}\b'.format(re.escape(comando)),
                           prompt, re.IGNORECASE)
    if not coincidencia==None:
        print(coincidencia)
        data.append(coincidencia)
    else:
        pass

if not data:
    print('Lo siento, no lo comprendo')
else:
    pass

    
