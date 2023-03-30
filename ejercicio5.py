import hashlib

class Nodo:
    def __init__(self, value):
        self.value=value
        self.next=None

class Encriptar:
    
    def __init__(self):
        self.tabla_hash_encriptacion = self.__generar_tabla_hash()
        self.tabla_hash_desencriptacion = {v: k for k, v in self.tabla_hash_encriptacion.items()}
        
    def __generar_tabla_hash(self):
        tabla_hash = {}
        for i in range(32, 126):
            key = chr(i)
            value = hashlib.sha256(key.encode()).hexdigest()[:8]
            tabla_hash[key] = value
        return tabla_hash

    def encriptar(self, cadena):
        cadena_encriptada = ""
        for caracter in cadena:
            valor_encriptado = self.tabla_hash_encriptacion.get(caracter)
            if valor_encriptado is not None:
                cadena_encriptada += valor_encriptado
            else:
                cadena_encriptada += caracter
        return cadena_encriptada

def desencriptar(self, cadena_encriptada):
    cadena_desencriptada = ""
    i = 0
    while i < len(cadena_encriptada):
        grupo = cadena_encriptada[i:i+8]
        valor_original = self.tabla_hash_desencriptacion.get(grupo)
        if valor_original is not None:
            cadena_desencriptada += valor_original
        else:
            cadena_desencriptada += grupo
        i += 8
    return cadena_desencriptada


# Experimentación

if __name__ == "__main__":

    encriptador = Encriptar()

    cadena_original = "Hola, ¿cómo estás?"
    cadena_encriptada = encriptador.encriptar(cadena_original)
    print(cadena_encriptada)

    cadena_desencriptada = encriptador.desencriptar(cadena_encriptada)
    print(cadena_desencriptada)


