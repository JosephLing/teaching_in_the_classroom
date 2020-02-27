#!/bin/python3
from turtle import *
from random import randint
from time import sleep

tracer(0)
hideturtle()
penup()
goto(-140, 140)

for step in range(12):
  write(step, align="center")
  right(90)
  forward(10)
  pendown()
  forward(150)
  penup()
  backward(160)
  left(90)
  forward(20)


ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 80)
bob.pendown()


right(90)
fd(200)
right(90)
fd(150)
winner = False
for i in range(100):
  if ada.position()[0] > 100 and not winner:
    winner = True
    write("winner red")
  
  if bob.position()[0] > 100 and not winner:
    winner = True
    write("winner blue")
  
  sleep(0.05)
  
  ada.fd(randint(1,5))
  bob.fd(randint(1,5))
  update()