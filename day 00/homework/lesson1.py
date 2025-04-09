from turtle import *


#we want to paint a house

#step 1: draw a square
begin_fill()
color("blue")
speed(30)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square
#drawing a door
begin_fill()
forward(70)
color("cyan")
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#draw a window


penup() 
goto(150,150)
pendown()
color("grey")

left(30)
forward(40)
left(90)
forward(40)
penup()
goto(150,150)
pendown()


forward(40)
right(90)
forward(40)
penup()
goto(170,150)
pendown()
forward(40)
penup()
goto(150,130)
pendown()

left(90)
forward(40)
#first window is done
penup()
goto(50,150)
pendown()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
penup()
goto(30,150)
pendown()
right(90)
forward(40)
penup()
goto(10,130)
pendown()
left(90)
forward(40)
#second window is done



exitonclick()