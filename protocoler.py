
steps=[]
numsteps=[]

print('''
Bienvenido al protocoler, aquí usted podrá crear protocolos, agregando pasos y subpasos para poder crear un protocolo.
''')
issue=input("¿Para qué será el protocolo?\nEste es un protocolo para: ")

menuer=True

while menuer==True:
    truemenu=int(input('''
    Bien, ahora, por favor, eliga una de las siguientes opciones (introduzca el número correspondiente)

    1.- Introducir un paso/subpaso principal
    2.- Borrar paso/subpaso específico
    3.- Mostrar protocolo
    4.- Guardar protocolo
    5.- Finalizar programa
    '''))

    if truemenu==1:
        x=input("Por favor, ingrese el número de paso o subpaso que quiere agregar: ")
        step=input("Ingrese su información por favor: ")
        steps.append(x+".- "+step)
        numsteps.append(x)
        truemenu=0
        
    elif truemenu==2:
        steps.sort()
        numsteps.sort()
        for i in range (len(steps)):
            print(steps[i])
        x=input("Introduzca el número de su paso/subpaso para borrar: ")
        posi=(numsteps.index(x))
        steps.pop(posi)
        numsteps.pop(posi)
    elif truemenu==3:
        steps.sort()
        for i in range (len(steps)):
            print(steps[i])
    elif truemenu==4:
        steps.sort()
        file = open("protocolo.txt", "w")
        file.write("Este es un protocolo para "+issue+"\n")
        for i in range (len(steps)):
            file.write(steps[i] + "\n")
        file.close()
    elif truemenu==5:
        print("Muchas gracias por utilizar este programa, un abrazo virtual.")
        menuer=False
