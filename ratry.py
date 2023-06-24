import math

# Ejemplo de Razones trigonométricas
cateto_contiguo=59.8
cateto_opuesto=33.6
print("Cateto contiguo: ", cateto_contiguo)
print("Cateto opuesto: ", cateto_opuesto)
hipotenusa=math.sqrt(cateto_contiguo**2+cateto_opuesto**2)
print("Hipotenusa: ", hipotenusa)

# Datos
angulo = 30
hipotenusa = 10

print("Angulo: ", angulo)
print("Hipotenusa: ", hipotenusa)

# Cálculos
cateto_opuesto = hipotenusa * math.sin(math.radians(angulo))
cateto_contiguo = hipotenusa * math.cos(math.radians(angulo))
print("Cateto opuesto: ", cateto_opuesto)
print("Cateto contiguo: ", cateto_contiguo)
