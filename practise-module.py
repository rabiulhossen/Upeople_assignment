import turtle #turtle used for graphical interface
bob = turtle.Turtle()
print(bob)
turtle.mainloop() #mainloop tells the window to wait for the user to do something
""""
bob.fd(100) #bob.fd is a method
bob.lt(80) 
bob.fd(100)"""
# single line comment """ multi line comment

"""
for i in range(4):
    bob.fd(100)
    wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
"""

#draw square  using Turtle Programming
import turtle 
skk = turtle.Turtle()

for i in range(4):
	skk.forward(50)
	skk.right(90)
	
turtle.done()


# draw star

star= turtle.Turtle()
star.right(75)
star.forward(100)
for j in range(4):
    star.right(144)
    star.forward(100)
    
turtle.done()
    