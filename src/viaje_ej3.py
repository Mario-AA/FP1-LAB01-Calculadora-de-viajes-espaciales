edad = int(input("Ingrese su edad: "))
nivel_fisico = int(input("Ingrese su nivel físico: "))
while nivel_fisico<1 or nivel_fisico>10:
    nivel_fisico = int(input("Nivel no válido, ingréselo denuevo: "))
if edad < 18:
    print("Has de ser mayor de edad")
elif nivel_fisico < 5:
    print ("Debes estar en mejor forma")
else:
    print("¡Listo para despegar!")