print("Ejercicio 4")

filas = int(input("Digite la cantidad de filas: "))

for i in range (1,filas+1):
    if i == 1:
        p = str(i)
    else:
        p = p +str(i)
    print(p)
