edat=int(input("Quina edat tens?"))
entrada=int(input("Tens l'entrada?"))
roba=(int(input("Quina roba portes? (1=pantalo blanc, 2=camisa blanca, 3=zapates blancs)")))

if edat>=18 and entrada==1 and roba==1:
    print("Pots entrar al discoteca")
else:
    print("No pots entrar al discoteca")


print("Programa Finalitzat")