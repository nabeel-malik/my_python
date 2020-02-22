import turtle


turtle.setup()
turtle.screensize (1850, 1100, 'black')

turtle.shape('turtle')
turtle.color('green')
turtle.up()
turtle.backward(380)
turtle.left(90)
turtle.forward(350)
turtle.right(90)
turtle.down()



for iteration in range (10):

    for side in range (6):
        turtle.forward(50)
        turtle.right(60)

    for side in range (6):
        turtle.forward(50)
        turtle.left(60)

    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.left(60)


turtle.done()