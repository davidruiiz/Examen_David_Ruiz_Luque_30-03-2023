class Nodo:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class TDAPolinomio:
    def __init__(self):
        self.primero = None

    def agregar(self, coeficiente, exponente):
        nuevo = Nodo(coeficiente, exponente)
        if self.primero is None:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.primero
        while actual is not None:
            print(actual.coeficiente, 'x^', actual.exponente, end=' ')
            if actual.siguiente is not None:
                print('+', end=' ')
            actual = actual.siguiente
        print()

    def evaluar(self, x):
        actual = self.primero
        suma = 0
        while actual is not None:
            suma += actual.coeficiente * (x ** actual.exponente)
            actual = actual.siguiente
        return suma
    
    def sumar(self, p2):
        p3 = TDAPolinomio()
        actual = self.primero
        while actual is not None:
            p3.agregar(actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        actual = p2.primero
        while actual is not None:
            p3.agregar(actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        return p3
    
    def restar(self, p2):
        p3 = TDAPolinomio()
        actual = self.primero
        while actual is not None:
            p3.agregar(actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        actual = p2.primero
        while actual is not None:
            p3.agregar(-actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        return p3
    
    def dividir(self, p2):
        p3 = TDAPolinomio()
        actual = self.primero
        while actual is not None:
            p3.agregar(actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        actual = p2.primero
        while actual is not None:
            p3.agregar(-actual.coeficiente, actual.exponente)
            actual = actual.siguiente
        return p3
    
    def eliminar_termino(self, exponente):
        actual = self.primero
        if actual.exponente == exponente:
            self.primero = actual.siguiente
            return
        while actual.siguiente is not None:
            if actual.siguiente.exponente == exponente:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
        return None
    
    def buscar_termino(self, exponente):
        
        actual = self.primero
        while actual is not None:
            if actual.exponente == exponente:
                return actual
            actual = actual.siguiente
        return None
    

if __name__ == '__main__':
    p1 = TDAPolinomio()
    p1.agregar(3, 2)
    p1.agregar(2, 1)
    p1.agregar(4, 0)
    print('Polinomio 1')
    p1.mostrar()
    print('Evaluar en x = 2')
    print(p1.evaluar(2))
    print()
    
    p2 = TDAPolinomio()
    p2.agregar(1, 1)
    p2.agregar(3, 0)
    print('Polinomio 2')
    p2.mostrar()
    print('Evaluar en x = 3')
    print(p2.evaluar(3))
    print()
    
    p3 = p1.sumar(p2)
    print('Suma')
    p3.mostrar()
    print()
    
    p3 = p1.restar(p2)
    print('Resta')
    p3.mostrar()
    print()
    
    p3 = p1.dividir(p2)
    print('División')
    p3.mostrar()
    print()
    
    p3 = p1.buscar_termino(2)
    print('Buscar termino')
    print(p3.coeficiente, p3.exponente)
    print()
    
    p1.eliminar_termino(1)
    print('Eliminar termino')
    p1.mostrar()
    print()