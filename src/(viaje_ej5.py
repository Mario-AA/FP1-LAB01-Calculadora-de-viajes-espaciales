simular = "s"
while simular == "s":
    distancia_km = int(input("Ingrese la distancia a la que se encuentre el destino: ")) # distancia Tierra - Luna
    velocidad_kmh = int(input("Ingrese la velocidad que llevará su nave: "))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    simular = input("¿Quieres hacer otra simulación? (s/n)")