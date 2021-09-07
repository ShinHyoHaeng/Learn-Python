import turtle as t

angle = 45
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(200):
    print(x)
    t.forward(x)
    t.left(angle)
