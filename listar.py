from archivoCSV import archivoCSV

estudiantes = archivoCSV("estudiantes.csv")
apoderados = archivoCSV("apoderados.csv")
asignaturas = archivoCSV("asignaturas.csv")
actividades = archivoCSV("actividades.csv")
incripcionasignaturas = archivoCSV("incripcionasignaturas.csv")
incripcionactividades = archivoCSV("incripcionactividades.csv")

estudiantes.listar()
apoderados.listar()
asignaturas.listar()
actividades.listar()
incripcionasignaturas.listar()
incripcionactividades.listar()