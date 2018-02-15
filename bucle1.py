num1=int(input("Introduce un numero: "))
num2=int(input("Introduce otro mayor al anterior: "))
nums=0
if num1>num2:
    print("No es mayor")
else:
    for n in range (num1,num2+1):
        nums=n*2
        if n%2==0:
            print ("Es par el",n)
        else:
            print ("Es impar el",n)
