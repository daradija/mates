import math

# Ejemplo de Razones trigonométricas

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
