num = int(input("Introduce un número entero mayor que cero: "))

if num <=0:
    print("no valido")
else:
    print("Los divisores de",num,"son...")
    for n in range(1, num+1):
        if num % n==0:
            print(n)
