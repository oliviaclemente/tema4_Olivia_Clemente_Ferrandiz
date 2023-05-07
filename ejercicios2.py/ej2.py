import random


class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre


class Vehiculo(Recurso):
    def __init__(self, nombre, tipo):
        super().__init__(nombre)
        self.tipo = tipo


class Mision:
    def __init__(self, tipo, planeta, general):
        self.tipo = tipo
        self.planeta = planeta
        self.general = general


class MisionAltaPrioridad(Mision):
    def __init__(self, tipo, planeta, general):
        super().__init__(tipo, planeta, general)


class MisionBajaPrioridad(Mision):
    def __init__(self, tipo, planeta, general):
        super().__init__(tipo, planeta, general)


class AdministradorMisiones:
    def __init__(self):
        self.recursos_asignados = []

    def asignar_recursos(self, mision):
        if isinstance(mision, MisionAltaPrioridad):
            self.asignar_recursos_manualmente(mision)
        else:
            self.asignar_recursos_automaticamente(mision)

    def asignar_recursos_manualmente(self, mision):
        if mision.tipo == "exploracion":
            scout_troopers = Recurso("Scout Trooper")
            speeder_bike = Vehiculo("Speeder Bike", "Terrestre")

            self.recursos_asignados.append(scout_troopers)
            self.recursos_asignados.append(speeder_bike)

        elif mision.tipo == "contencion":
            stormtroopers = Recurso("Stormtrooper")
            vehiculos = [Vehiculo("AT-AT", "Terrestre"), Vehiculo("AT-RT", "Terrestre"),
                         Vehiculo("AT-TE", "Terrestre"), Vehiculo("AT-DP", "Terrestre"),
                         Vehiculo("AT-ST", "Terrestre")]

            self.recursos_asignados.append(stormtroopers)
            self.recursos_asignados.extend(vehiculos)

        elif mision.tipo == "ataque":
            stormtroopers = Recurso("Stormtrooper")
            vehiculos = [Vehiculo("AT-AT", "Terrestre"), Vehiculo("AT-RT", "Terrestre"),
                         Vehiculo("AT-TE", "Terrestre"), Vehiculo("AT-DP", "Terrestre"),
                         Vehiculo("AT-ST", "Terrestre"), Vehiculo("AT-M6", "Terrestre"),
                         Vehiculo("AT-MP", "Terrestre"), Vehiculo("AT-DT", "Terrestre")]

            self.recursos_asignados.append(stormtroopers)
            self.recursos_asignados.extend(vehiculos)

    def asignar_recursos_automaticamente(self, mision):
        if mision.tipo == "exploracion":
            scout_troopers = Recurso("Scout Trooper")
            speeder_bike = Vehiculo("Speeder Bike", "Terrestre")

