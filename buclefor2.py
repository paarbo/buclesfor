num = int(input("Introduce un número entero mayor que cero: "))

if num <=0:
    print("no valido")
else:
    print("Los divisores de",num,"son", end=" ")
    for i in range(1, num + 1):
        if num % i==0:
            print(i, end=" ")
