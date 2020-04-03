import math

x1=int(input("Digite una coordenada x1 positiva"))
x2=int(input("Digite una coordenada x2 positiva"))
y1=int(input("Digite una coordenada y1 positiva"))
y2=int(input("Digite una coordenada y2 positiva"))

if x1>0 and x2>0 and y1>0 and y2>0:
    formula=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("La distancia ordinaria entre dos puntos de un espacio euclídeo es..",formula)
else:
    print("El sistema solo admite valores positivos")    