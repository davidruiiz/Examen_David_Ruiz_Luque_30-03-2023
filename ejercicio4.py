import unittest

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("¡Alumno creado con éxito!")

    def calificacion(self):
        if self.nota >= 5:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} ha suspendido con una nota de {self.nota}.")

    def __str__(self):
        return f"Nombre: {self.nombre}, Nota: {self.nota}"


# Pruebas

class TestAlumno(unittest.TestCase):

    def setUp(self):
        self.alumno1 = Alumno("Juan", 8)
        self.alumno2 = Alumno("Pedro", 4)

    def test_calificacion(self):
        self.assertEqual(self.alumno1.calificacion(), None)
        self.assertEqual(self.alumno2.calificacion(), None)

    def test_str(self):
        self.assertEqual(str(self.alumno1), "Nombre: Juan, Nota: 8")
        self.assertEqual(str(self.alumno2), "Nombre: Pedro, Nota: 4")

# Experimentación

if __name__ == "__main__":
    alumno1 = Alumno("Juan", 8)
    print(alumno1)
    alumno1.calificacion()
    alumno2 = Alumno("Pedro", 4)
    print(alumno2)
    alumno2.calificacion()

    unittest.main()

