print("Ejercicio 3")

n1 = float(input("Digite el valor de la primera nota: "))
n2 = float(input("Digite el valor de la segunda nota: "))
n3 = float(input("Digite el valor de la tercera nota: "))
n4 = float(input("Digite el valor de la cuarta nota: "))
n5 = float(input("Digite el valor de la quinta nota: "))

if (n1 >5) or (n2>5) or (n3>5) or (n4>5) or (n5>5):
    print("Error al digitar las notas")
else:
    total = (n1*0.15 + n2*0.2 + n3*0.15 + n4*0.3 + n5*0.2) 

    if total < 2.0:
        print("No puede habilitar")
    elif total < 3.0:
        print("Reprobó")
    elif total >= 3.0:
        print("Aprobó")
    else:
        print("Felicitaciones por su desempeño académico.")