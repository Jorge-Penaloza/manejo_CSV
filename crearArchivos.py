from archivoCSV import archivoCSV

estudiantes = archivoCSV("estudiantes.csv")
estudiantes.crearCabecera("nombre","apellido","rut","direccion","anio")

apoderados = archivoCSV("apoderados.csv")
apoderados.crearCabecera("nombre","apellido","rut","direccion","anio")

incripcionasignaturas = archivoCSV("incripcionasignaturas.csv")
incripcionasignaturas.crearCabecera("rut","codigo")

incripcionactividades = archivoCSV("incripcionactividades.csv")
incripcionactividades.crearCabecera("rut","codigo")

asignaturas = archivoCSV("asignaturas.csv")
asignaturas.crearCabecera("codigo","descripcion", "plan")

actividades = archivoCSV("actividades.csv")
actividades.crearCabecera("codigo","descripcion", "plan")