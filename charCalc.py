
fuerza = 8
destreza = 8
constitucion = 8
inteligencia = 8
sabiduria = 8
carisma = 8

puntos = 30

print("""Listado de caracteristicas:\n 
\t* str ---> Fuerza
\t* dex ---> Destreza
\t* con ---> Constitucion
\t* int ---> Inteligencia
\t* wis ---> Sabiduria
\t* cha ---> Carisma""")
    
while puntos >= 0:
    caracteristica = input("Ingrese la caracteristica segun su abreviatura en ingles: ")
    caracteristica = caracteristica.lower()
    # CALCULO DE LOS PUNTOS GASTADOS #
    valor_gastado = int(input("Ingrese los puntos a gastar: "))
    
    resto = puntos - valor_gastado
    print("\nQuedan: ", resto, "para gastar")
    puntos = resto
    
    # CONDICIONALES PARA SUMAR LOS PUNTOS A DETERMINADA CARACTERISTICA #
    
    # CONDICIONAL DE LA FUERZA #
    if caracteristica == "str" and valor_gastado <= 5:
        fuerza += valor_gastado
        print("\nLa fuerza es de: ", fuerza)
    elif caracteristica == "str" and valor_gastado == 7:
        fuerza = 14
        print("\nLa fuerza es de: ", fuerza)
    elif caracteristica == "str" and valor_gastado == 9:
        fuerza = 15
        print("\nLa fuerza es de: ", fuerza)
    
    # CONDICIONAL DE LA DESTREZA # 
    if caracteristica == "dex" and valor_gastado <= 5:
        destreza += valor_gastado
        print("\nLa destreza es de: ", destreza)
    elif caracteristica == "dex" and valor_gastado == 7:
        destreza = 14
        print("\nLa destreza es de: ", destreza)
    elif caracteristica == "dex" and valor_gastado == 9:
        destreza = 15
        print("\nLa destreza es de: ", destreza)
  
    # CONDICIONAL DE LA CONSTITUCION #    
    if caracteristica == "con" and valor_gastado <= 5:
        constitucion += valor_gastado
        print("\nLa constitucion es de: ", constitucion)
    elif caracteristica == "con" and valor_gastado == 7:
        constitucion = 14
        print("\nLa constitucion es de: ", constitucion)
    elif caracteristica == "con" and valor_gastado == 9:
        constitucion = 15
        print("\nLa constitucion es de: ", constitucion)
   
    # CONDICIONAL DE LA INTELIGENCIA #   
    if caracteristica == "int" and valor_gastado <= 5:
        inteligencia += valor_gastado
        print("\nLa inteligencia es de: ", inteligencia)
    elif caracteristica == "int" and valor_gastado == 7:
        inteligencia = 14
        print("\nLa inteligencia es de: ", inteligencia)
    elif caracteristica == "int" and valor_gastado == 9:
        inteligencia = 15
        print("\nLa inteligencia es de: ", inteligencia)
   
    # CONDICIONAL DE LA SABIDURIA #
    if caracteristica == "wis" and valor_gastado <= 5:
        sabiduria += valor_gastado
        print("\nLa sabiduria es de: ", sabiduria)
    elif caracteristica == "wis" and valor_gastado == 7:
        sabiduria = 14
        print("\nLa sabiduria es de: ", sabiduria)
    elif caracteristica == "wis" and valor_gastado == 9:
        sabiduria = 15
        print("\nLa sabiduria es de: ", sabiduria)
    
    # CONDICIONAL DEL CARISMA #    
    if caracteristica == "cha" and valor_gastado <= 5:
        carisma += valor_gastado
        print("\nEl carisma es de: ", carisma)
    elif caracteristica == "cha" and valor_gastado == 7:
        carisma = 14
        print("\nEl carisma es de: ", carisma)
    elif caracteristica == "cha" and valor_gastado == 9:
        carisma = 15
        print("\nEl carisma es de: ", carisma, "\n")
    
    
    # CONDICIONAL PARA SALIR DEL BUCLE AL LLEGAR A 0 o AL PASARSE #
    if resto == 0:
        print("\nCaracteristicas Finales: ")
        print("\nFuerza: ", fuerza)
        print("Destreza: ", destreza)
        print("Constitucion: ", constitucion)
        print("Inteligencia: ", inteligencia)
        print("Sabiduria: ", sabiduria)
        print("Carisma: ", carisma)
        break
    elif resto < 0:
        print("\nGastó puntos de más")
        break
