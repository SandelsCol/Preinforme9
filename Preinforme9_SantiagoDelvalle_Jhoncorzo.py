Numero=int(input("Digite un número de 4 cifras"))  

if Numero >= 1000 and Numero < 10000:

    c4= Numero%10
    c3=int((Numero%100)/10)
    c2=int((Numero%1000)/100)
    c1=int((Numero-(Numero%100))/1000)

    print(str(c4)+str(c3)+str(c2)+str(c1)) 
else:
    print("El sistema solo trabaja con numeros de cuatro cifras")   