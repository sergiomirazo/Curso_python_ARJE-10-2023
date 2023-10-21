class Empleados:
    def __init__(self, nombre, clave, nomina, cel):
        self.nombre = nombre
        self.clave = clave
        self.nomina = nomina
        self.cel = cel

    def deposito(self, cantidad):
        self.nomina += cantidad

    def impuestos(self, cantidad):
        self.nomina -= cantidad

    def aviso(self):
        print(f"Mensaje enviado a {self.cel}")


def impuesto(salario_anual):
    if salario_anual<123580.80:
        return 0.0192
    elif salario_anual>123580.80 and salario_anual<249243.12:
        return 0.064
    elif salario_anual>249243.12 and salario_anual<392840.52:
        return 0.1088
    elif salario_anual>392840.52 and salario_anual<750000.00:
        return 0.16
    else:
        return None

e1 = Empleados('Juan Perez', 'DNSAJND2342', 16000, '6625656779')
print(e1.nomina)
impuesto_e1 = impuesto(e1.nomina*12)
print(impuesto_e1)
e1.impuestos(impuesto_e1*e1.nomina)
print(e1.nomina)

print(f"Clave anterior: {e1.clave}")
e1.clave ='ABBA8787'
print(f"Clave nueva: {e1.clave}")

nombres_empleados = ['Juan Lopez', 'Maria Astorga', 'Itsel Hernandez',
                     'Rodrigo Perez', 'Ivonne Garcia', 'Ana Estrada']
cel_empleados = ['667889774', '662656463', '6623434123',
                 '64676453453', '6467425523', '44543434']

empleados = [Empleados(x, 'DNSAJND2342', 16000, '6625656779') for x in nombres_empleados]
empleados[1].cel = '6462323455'
for objeto in empleados:
    print(objeto.nombre, objeto.nomina, objeto.clave, objeto.cel)
