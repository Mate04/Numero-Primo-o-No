#Cre
separador = "-" * 20 
vuelta = 0
#declaramos una lista para guardar los numeros primos y los no primos
primos = []
noPrimos = []
#inicializamos la primera variable para que empiece a contar
validar = int(input("\033[36m"+"Ingrese un numero \no 0 para finalizar programa \n"))
while validar != 0:
    if vuelta > 0:
        print("\033[36m"+separador)
        validar = int(input("\033[36m"+"Ingrese un nuevo numero \no 0 para salir \n"))
    vuelta =+ vuelta + 1
    if validar > 0:
        for i in range(validar+1):
            if i != 0 and i > 1:
                result = validar % (i)
                if validar != i and result == 0:
                    print("\033[31m"+"El numero "+str(validar)+" NO es primo")
                    noPrimos.append(validar)
                    break  
                elif validar == i:
                    print("\033[32m"+"El numero "+str(validar)+" es primo")
                    primos.append(validar)
                    break
                elif validar < 0:
                    print("\033[31m"+"Los numero negativos como "+str(validar)+" NO son numeros Primo")
            elif validar == 1:
                print("\033[31m"+"El numero "+str(validar)+" NO es un numero Primo")
                break
    elif validar < 0:
        print("\033[31m"+"El numero "+str(validar)+" NO es un numero Primo")
print("\033[36m"+separador)
print("Vueltas dadas: "+str(vuelta))
print("\033[36m"+separador)
if len(primos) > 0:
    print("\033[32m"+"La cantidad de numeros primos son: "+str(len(primos))+ "\ny son: ")
    for i in primos:
        print(i)
else:
    print("\033[32m"+"No hubo numeros primos")
print("\033[36m"+separador)

if len(noPrimos) > 0:
    print("\033[33m"+"La cantidad de numeros no primos son: "+str(len(noPrimos))+ "\ny son: ")
    for i in noPrimos:
        print(i)
else:
    print("\033[33m"+"No hubo numeros no primos")
print("\033[36m"+separador)
