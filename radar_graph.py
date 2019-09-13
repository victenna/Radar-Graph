import	turtle
import random
import time
wn=turtle.Screen()
s=turtle.Shape('compound')
turtle.tracer(2)
t1=turtle.Turtle()
t1.hideturtle()
t1.color('white')
t1.goto(0,0)
t1.pensize(2)
t2=turtle.Turtle()
t2.hideturtle()
t2.color('white')
turtle.bgcolor('black')

Text_font=('times New Roman', 15,'bold')
t2.up()
t3=turtle.Turtle()
t3.hideturtle()
t3.pensize(5)
t3.up()
t3.color('gold')
x=[0,0,0,0,0,0]
y=[0,0,0,0,0,0]
point=[176,80,56,48,40,176]
coord=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
Q=5
t3.up()
t3.goto(0,0)
for n in range(6):
    t3.up()
    t3.goto(0,0)
    t3.setheading(360/Q*n)
    t3.fd(point[n])
    x[n]=t3.xcor()
    y[n]=t3.ycor()
    print(x[n],y[n])
    t3.setposition(x[n],y[n])
    coord[n]=t3.position()
    print(coord[n])
    
t3.up()
t3.goto(coord[0])
t3.down()
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
for i in range (1,6):
    t3.left(0)
    t3.goto(coord[i])
t3.left(0)
t3.goto(176,0)

for n in range(Q):
    t2.up()
    t2.goto(0,0)
    t2.setheading(360/Q*n)
    t2.fd(200)
    t2.down()
    t2.write('50',font=Text_font)
    t2.fd(40)
    if n==0:
        t2.write('Chrome 44%',font=Text_font)
    if n==1:
        t2.write('Safari 20%',font=Text_font)
    if n==2:
        t2.write('Edge 14%',font=Text_font)
    if n==3:
        t2.write('Firefox 48%',font=Text_font)
    if n==4:
        t2.write('Other 40%',font=Text_font)

t2.up()
t2.goto(-200,300)
t2.down()
t2.write('Browser Statistics Radar Graph',font=('times New Roman',25,'bold')) 
        
for i in range (Q):
    t1.goto(0,0)
    t1.setheading(360/Q*i)
    for j in range (5):
        t1.setheading(360/Q*i)
        t1.fd(40)
        t1.setheading(90+360/Q*i)
        t1.down()
        t1.fd(10)
        t1.fd(-10)
   

