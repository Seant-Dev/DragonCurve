from turtle import *    #Biblioteca para dibujar

def curveRec(n):
    if n == 0:
        return []
    else:
        c = curveRec(n - 1)
        r = c[::-1]
        i = ['I' if g == 'D' else 'D' for g in r]
        return c + ['I'] + i

for i in range(6):
    print('orden {0}: {1}'.format(i, ''.join(curveRec(i))))

def dragonCurve(n, x):
    fd(x)
    for g in curveRec(n):
        if g == 'I':
            lt(90)
        else:
            rt(90)
        fd(x)

bgcolor("#17202A")  #Color del fondo en Turtle

#-----------------Primer dibujo
penup()
goto(-200,-200)     #Posicion para iniciar dibujo
pendown()
hideturtle()
pensize(2)
color('#EBCD21')    #Colores en Hexa
speed('fastest')    #Velocidad de Dibujo
setheading(-45)
dragonCurve(9,3)

#-----------------Segundo dibujo
penup()
goto(-100,-100)     #Posicion para iniciar dibujo
pendown()
hideturtle()
pensize(2)
color('#EB4BB2')    #Colores en Hexa
speed('fastest')    #Velocidad de Dibujo
setheading(-45)
dragonCurve(9,3)

#-----------------Tercer dibujo
penup()
goto(0,0)           #Posicion para iniciar dibujo
pendown()
hideturtle()
pensize(2)
color('#34E3EB')    #Colores en Hexa
speed('fastest')    #Velocidad de Dibujo
setheading(-45)
dragonCurve(9,3)

done()