class Personaje:
    def __init__(self, salud, fuerza, vigor, nombre, equipo):
        """
            Notación camelCase: para variables
        """
        self.salud = salud
        self.fuerza = fuerza
        self.vigor = vigor
        self.nombre = nombre
        self.equipo = equipo

    def herido(self):
        self.salud -= 10

    def curar(self):
        self.salud += 10

    def __str__(self):
        print(f"Nombre: {self.nombre}| Salud: {self.salud}|Fuerza: {self.fuerza}| Vigor: {self.vigor}")


p1 = Personaje(100, 7, 50, "Jhon", ["Espada", "Escudo"])
p1.herido()
print(p1.salud)
print(str(p1))
