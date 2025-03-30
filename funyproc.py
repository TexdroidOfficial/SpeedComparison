def main():
    print("UCAB Programa elaborado por Stephanie Vielma")
    
    res = float
    
    def validar(num):
        if (num >= 100) and (num <= 999):
            bool = True
        else:
            bool = False
        return bool
    
    def transform(x, y):
        res = (x/y)
        return res
    
    def speed(z, t):
        nonlocal res
        res = (z/t)
        
    def mayor(q, h):
        if (q > h):
            bool = 1
        elif (q < h):
            bool = 2
        else:
            bool = 3
        return bool

    print("Indique un numero entero positivo de 3 digitos de distancia 1")
    d1 = int(input())
    print("Indique un numero entero positivo de 3 digitos de tiempo 1")
    t1 = int(input())
    print("Indique un numero entero positivo de 3 digitos de distancia 2")
    d2 = int(input())
    print("Indique un numero entero positivo de 3 digitos de tiempo 2")
    t2 = int(input())
    
    if (validar(d1)) and (validar(d2)) and (validar(t1)) and (validar(t2)) == False:
        print("Error, los valores deben ser enteros positivos de 3 digitos")
    else:
        d1k = transform(d1, 1000)
        t1h = transform(t1, 60)
        d2k = transform(d2, 1000)
        t2h = transform(t2, 60)
        speed(d1k, t1h)
        v1 = res
        speed(d2k, t2h)
        v2 = res
        if mayor(v1, v2) == 1:
            winner = "El mas veloz es el vehiculo 1"
        elif mayor(v1, v2) == 2:
            winner = "El mas veloz es el vehiculo 2"
        else:
            winner = "Ambos vehiculos tienen la misma velocidad"
        
        print("La distancia 1 en metros es: ", d1)
        print("El tiempo 1 en minutos es: ", t1)
        print("La distancia 1 en kilometros es: ", d1k)
        print("El tiempo 1 en horas es: ", t1h)
        print("La distancia 2 en metros es: ", d2)
        print("El tiempo 2 en minutos es: ", t2)
        print("La distancia 2 en kilometros es: ", d2k)
        print("El tiempo 2 en horas es: ", t2h)
        print("La velocidad del vehiculo 1 es: ", v1, "Km/h")
        print("La velocidad del vehiculo 2 es: ", v2, "Km/h")
        print(winner)
    
main()