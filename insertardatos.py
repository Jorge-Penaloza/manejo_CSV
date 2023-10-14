from archivoCSV import archivoCSV

estudiantes = archivoCSV("estudiantes.csv")
estudiantes.insertar("Jorge","Peñaloza","13834570-k","Las Camelias","2021")
estudiantes.insertar("Anais","Lopez","15321528-8","Las Magnolias","2022")

apoderados = archivoCSV("apoderados.csv")
apoderados.insertar("Segundo","Peñaloza","6525321-2","Las Camelias","2021")

asignaturas = archivoCSV("asignaturas.csv")
asignaturas.insertar("1","Ingles", "Verbos")
asignaturas.insertar("2","Matematica", "Integrales")

actividades = archivoCSV("actividades.csv")
actividades.insertar("1","Natacion", "5km por sesion")

incripcionasignaturas = archivoCSV("incripcionasignaturas.csv")
incripcionasignaturas.insertar("13834570-k","1")
incripcionasignaturas.insertar("13834570-k","2")
incripcionasignaturas.insertar("15321528-8","2")

incripcionactividades = archivoCSV("incripcionactividades.csv")
incripcionactividades.insertar("13834570-k","1")

