import math, time

# Ejemplo de Razones trigonométricas
cateto_contiguo=598
cateto_opuesto=336
print("Cateto contiguo: ", cateto_contiguo)
print("Cateto opuesto: ", cateto_opuesto)
hipotenusa=math.sqrt(cateto_contiguo**2+cateto_opuesto**2)
print("Hipotenusa: ", hipotenusa)


import turtle

# draw a circle
turtle.right(90)
turtle.penup()
turtle.forward(hipotenusa/4)
turtle.pendown()
turtle.left(90)
turtle.circle(hipotenusa/4)
turtle.penup()
turtle.left(90)
turtle.forward(hipotenusa/4)
turtle.pendown()


# get de current hour
import datetime
now = datetime.datetime.now()
hour=now.hour
minute=now.minute
second=now.second

# draw a clock hour bar
hourangle=hour/12*360+minute/60*360/12
turtle.right(hourangle)
turtle.forward(hipotenusa/8)
turtle.backward(hipotenusa/8)
turtle.left(hourangle)

# draw a clock minute bar
minuteangle=minute/60*360
turtle.right(minuteangle)
turtle.forward(hipotenusa/5)
turtle.backward(hipotenusa/5)
turtle.left(minuteangle)

# draw a clock second bar
# for ever
while True:
	secondangle=second/60*360
	turtle.right(secondangle)
	turtle.forward(hipotenusa/4)
	# sleep a second
	time.sleep(1)
	# tuttle erase mode
	turtle.undo()
	turtle.left(secondangle)
	now = datetime.datetime.now()
	second=now.second


turtle.done()

input("Press any key to continue")
turtle.penup()
turtle.goto(-cateto_contiguo/2,0)
turtle.pendown()

turtle.forward(cateto_contiguo)
turtle.left(90)
turtle.forward(cateto_opuesto)
turtle.left(90)
turtle.forward(cateto_contiguo)
turtle.left(90)
turtle.forward(cateto_opuesto)
turtle.left(90)

angulo=math.atan(cateto_opuesto/cateto_contiguo)
# radianes a grados
angulo=angulo*180/math.pi
turtle.left(angulo)
turtle.forward(hipotenusa)

turtle.done()
# pause until press a key
input("Press any key to finish")
