def comprobar_entrada_discoteca():
    edad = int(input("¿Edad? "))
    if edad < 18:
        print("Menor de edad")
        return False
    
    entrada = input("¿Entrada comprada? (si/no): ").lower().strip()
    if entrada not in ["si", "sí"]:
        print("Sin entrada")
        return False
    
    ropa = input("¿Ropa correcta? (si/no): ").lower().strip()
    if ropa not in ["si", "sí"]:
        print("Ropa incorrecta")
        return False
    
    print("Bienvenido!")
    return True


if __name__ == "__main__":
    comprobar_entrada_discoteca()
