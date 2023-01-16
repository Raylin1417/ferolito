import random
random.randint(0,10)
random=random.randint(0,10)
print("Tu número aleatorio es : ", random)
numero=int(input("Danos un número del 0 al 10 : "))
while random<11 :
    if numero< random :
        print(" Tu número es menor")
        numero=int(input("Danos un numero mas alto :"))
    if numero==random :
        print("BINGO")
        break
    if numero>random :
        print("Tu numero es mayor")
        numero=int(input("Danos un numero menor"))