num1=int(input("Introduce un numero: "))
num2=int(input("Introduce otro mayor al anterior: "))

if num1>num2:
    print("No es mayor")
else:
    for i in range (num1,num2):
        aux=i*2
        if i%2==0:
            print ("Es par el",i)
        else:
            print ("Es impar el",i)
