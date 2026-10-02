try:
    edat = int(input("Quina edat tens?"))
    entrada = (input("Tens l'entrada? (si/no)"))
    roba = input("Quina roba portes? (tot blanc)")

    if edat >= 18 and entrada == "si" and roba == "tot blanc":
        print("Pots entrar al discoteca")
    else:
        print("No pots entrar a la festa")
except ValueError:
    print("Si us plau, introdueix valors vàlids.")

print("Programa Finalitzat")

#prova final