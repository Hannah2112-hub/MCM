class OperacionesMatematicas:
    def mcd(self, x, y):
        while y:
            x, y = y, x % y
        return x

    def mcm(self, numeros):
        if any(a == 0 for a in numeros):
            raise ValueError("El MCM no está definido para cero.")

        resultado = numeros[0]
        for numero in numeros[1:]:
            resultado = abs(resultado * numero) // self.mcd(resultado, numero)
        return resultado
