class Ejercicio:

    def __init__(self, lista):
        self.lista = lista

    def __str__(self) -> str:
        return f"Lista: {self.lista}"

    def recorre_lista(self):
        print("Múltiplos de 10 y menores que 200:")
        multiples = [num for num in self.lista if num < 200 and num % 10 == 0]
        print(", ".join(str(num) for num in multiples))

        print("\n")

        for num in self.lista:
            if num > 300:
                break

        print("Lista ordenada:")
        self.ordena_lista()
        print(self.lista)

        print("\n")

    def ordena_lista(self):
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2 # dividimos la lista en dos
                left = arr[:mid] # parte izquierda
                right = arr[mid:] # parte derecha
                merge_sort(left) # ordenamos la parte izquierda
                merge_sort(right) # ordenamos la parte derecha 
                i = j = k = 0
                while i < len(left) and j < len(right): # recorremos las dos partes
                    if left[i] < right[j]: # si el elemento de la izquierda es menor que el de la derecha
                        arr[k] = left[i] # el elemento de la izquierda se agrega al arreglo
                        i += 1 # avanzamos en la parte izquierda
                    else:
                        arr[k] = right[j] # de lo contrario, el elemento de la derecha se agrega al arreglo
                        j += 1
                    k += 1
                while i < len(left): # si quedan elementos en la parte izquierda
                    arr[k] = left[i] # los agregamos al arreglo
                    i += 1 
                    k += 1 
                while j < len(right): # si quedan elementos en la parte derecha
                    arr[k] = right[j] # los agregamos al arreglo
                    j += 1
                    k += 1

        merge_sort(self.lista)

    def encuentra_valor(self, valor):
        if valor in self.lista:
            return f"El valor {valor} se encontró en el índice {self.lista.index(valor)}."
        else:
            return f"El valor {valor} no se encontró en la lista."



if __name__ == "__main__":
    lista = [18, 50, 210, 80, 145, 333, 70, 30]
    ej = Ejercicio(lista)

    ej.recorre_lista()
    ej.ordena_lista()
    print(ej.encuentra_valor(145))
