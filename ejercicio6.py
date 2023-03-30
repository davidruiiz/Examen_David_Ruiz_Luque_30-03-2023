class Node(object):
    info, sig = None, None

class ListaEnlazada(object):
    def __init__(self, cima=None):
        self.cima = cima

    def append(self, info):
        aux = Node()
        if self.cima:
            actual = self.cima
            while actual.sig:
                actual = actual.sig
            actual.sig = aux.info
        else:
            self.cima = aux.info

    def __iter__(self):
        actual = self.cima
        while actual:
            yield actual
            actual = actual.sig

    def __len__(self):
        actual = self.cima
        total = 0
        while actual:
            total += 1
            actual = actual.sig
        return total

    def __repr__(self):
        nodes = []
        actual = self.cima
        while actual:
            if actual.info is self.cima:
                nodes.append("[cima: %s]" % actual.info)
            elif actual.sig is None:
                nodes.append("[Tail: %s]" % actual.info)
            else:
                nodes.append("[%s]" % actual.info)
            actual = actual.sig
        return '-> '.join(nodes)
    
    def __getitem__(self, index):
        if index >= len(self) or index < 0:
            raise IndexError("Indice fuera de rango")
        actual = self.cima
        for i in range(index):
            actual = actual.sig
        return actual.info
    
    def __setitem__(self, index, info):
        if index >= len(self) or index < 0:
            raise IndexError("Indice fuera de rango")
        actual = self.cima
        for i in range(index):
            actual = actual.sig
        actual.info = info

class Matrix(object):
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matrix = [ListaEnlazada() for i in range(filas)]
        for row in self.matrix:
            for i in range(columnas):
                row.append(0)

    
    
    def menor(self, row, col):
        if self.filas != self.columnas:
            raise Exception("Matriz no cuadrada")
        result = Matrix(self.filas - 1, self.columnas - 1)
        r = 0
        for i in range(self.filas):
            if i == row:
                continue
            c = 0
            for j in range(self.columnas):
                if j == col:
                    continue
                result[r][c] = self[i][j]
                c += 1
            r += 1
        return result
    
    def determinante_iterativo(self):
        if self.filas != self.columnas:
            raise Exception("Matriz no cuadrada")
        if self.filas == 1:
            return self[0][0]
        if self.filas == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        result = 0
        for i in range(self.columnas):
            result += (-1) ** i * self[0][i] * self.menor(0, i).determinante_recursivo()
        return result
    
    def determinante_recursivo(self):
        if self.filas != self.columnas:
            raise Exception("Matriz no cuadrada")
        if self.filas == 1:
            return self[0][0]
        if self.filas == 2:
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        result = 0
        for i in range(self.columnas):
            result += (-1) ** i * self[0][i] * self.menor(0, i).determinante_recursivo()
        return result
        
        
if __name__ == '__main__':
    m = Matrix(3, 3)
    m[0][0] = 1
    m[0][1] = 2
    m[0][2] = 3
    m[1][0] = 4
    m[1][1] = 5
    m[1][2] = 6
    m[2][0] = 7
    m[2][1] = 8
    m[2][2] = 9
    print(m)
    print(m.determinante_iterativo())
    print(m.determinante_recursivo())