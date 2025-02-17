import turtle as trtl

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 0
xpos = -30
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 1 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos+10,ypos+30)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots = num_dots+2
while (1<num_dots<=2):
  ladybug.penup()
  ladybug.goto(10,-40)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(20,-10)
  ladybug.pendown()
  ladybug.circle(2)
  num_dots = num_dots+2


  # position next dots
  xpos = ypos + 25
  xpos = xpos + 5
  num_dot = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()