import unittest

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("¡Alumno creado con éxito!")

    def calificacion(self):
        if self.nota >= 5:
            return f"{self.nombre} ha aprobado con una nota de {self.nota}."
        else:
            return f"{self.nombre} ha suspendido con una nota de {self.nota}."

# Pruebas

class TestAlumno(unittest.TestCase):

    def setUp(self):
        self.alumno1 = Alumno("Juan", 8)
        self.alumno2 = Alumno("Pedro", 4)

    def test_nombre(self):
        self.assertEqual(self.alumno1.nombre, "Juan")
        self.assertEqual(self.alumno2.nombre, "Pedro")

    def test_nota(self):
        self.assertEqual(self.alumno1.nota, 8)
        self.assertEqual(self.alumno2.nota, 4)

    def test_calificacion(self):
        self.assertEqual(self.alumno1.calificacion(), "Juan ha aprobado con una nota de 8.")
        self.assertEqual(self.alumno2.calificacion(), "Pedro ha suspendido con una nota de 4.")


# Experimentación

if __name__ == "__main__":
    #creamos algunos alumnos
    alumno1 = Alumno("Juan", 8)
    alumno2 = Alumno("Pedro", 4)

    #ejecutamos el método calificación
    alumno1.calificacion()
    alumno2.calificacion()

    #ejecutamos las pruebas
    unittest.main()

    

