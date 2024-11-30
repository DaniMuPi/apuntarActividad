from cargarActividad import cargarActividad

def apuntarActividad(archivoActividad, nombreUsuario, estadoActividad):
    actividad_dict = cargarActividad(archivoActividad)
    if (nombreUsuario in actividad_dict):
        mensaje = "Este usuario ya está apuntado a la actividad."
    else: 
        with open(archivoActividad, 'a') as f:
            f.write(f"{nombreUsuario};{estadoActividad}\n")
        mensaje = f"El usuario se ha añadido correctamente como {estado}."
    return mensaje

