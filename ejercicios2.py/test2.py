from ej2 import AdministradorMisiones, MisionAltaPrioridad, MisionBajaPrioridad


# Crear el administrador de misiones
administrador = AdministradorMisiones()

# Crear misiones
mision_alta_prioridad = MisionAltaPrioridad("contencion", "Planeta A", "Darth Vader")
mision_baja_prioridad1 = MisionBajaPrioridad("exploracion", "Planeta B", "General 1")
mision_baja_prioridad2 = MisionBajaPrioridad("ataque", "Planeta C", "General 2")

# Asignar recursos a las misiones
administrador.asignar_recursos(mision_alta_prioridad)
administrador.asignar_recursos(mision_baja_prioridad1)
administrador.asignar_recursos(mision_baja_prioridad2)

# Mostrar recursos asignados a cada misión
print("Recursos asignados a la misión de alta prioridad:")
for recurso in administrador.recursos_asignados:
    print("- ", recurso.nombre)

print("")

print("Recursos asignados a la primera misión de baja prioridad:")
for recurso in administrador.recursos_asignados:
    print("- ", recurso.nombre)

print("")

print("Recursos asignados a la segunda misión de baja prioridad:")
for recurso in administrador.recursos_asignados:
    print("- ", recurso.nombre)

