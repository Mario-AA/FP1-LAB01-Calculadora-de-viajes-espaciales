"""
distancia_km = 384400  # distancia Tierra - Luna
velocidad_kmh = 5000
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = (tiempo_horas / 24)%7
tiempo_semanas = tiempo_horas // 24*7
print(f"Tardarías {tiempo_semanas} semanas y {tiempo_dias:.0f} días en llegar.")
"""