# Turtle window screen
import turtle

#create a screen object, save it as wn
wn = turtle.Screen()

# Title, background colour and size
wn.title("Air hockey")
wn.bgcolor("black") #The word colour must be used as th american spelling of the word color
wn.setup(width = 800, height = 600)

# switch turtle animation off
wn.tracer(0)

#Use a turtle to draw a bounding box
# Create a turtle called pen
pen = turtle.Turtle()

pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-350, -250)
pen.pendown()
pen.setheading(0)

#draw bounding box
pen.forward(700/3) #2nd white line from the left
pen.left(90)
pen.forward(500)
pen.left(90)

pen.forward(700/3) #2nd white line from the left
pen.left(90)
pen.forward(500)
pen.left(90)

pen.forward(340) #centre left line - 3rd white line from left
pen.left(90)
pen.forward(500)
pen.left(90)

pen.forward(340) #centre left line - 3rd white line from left
pen.left(90)
pen.forward(500)
pen.left(90)

pen.forward(360) #centre right line -4th white line from the left
pen.left(90)
pen.forward(500)
pen.left(90)

pen.forward(360) #centre right line - 4th white line from the left
pen.left(90)
pen.forward(500)
pen.left(90)

pen.forward(700*2/3) #5th white line from the left
pen.left(90)
pen.forward(500)
pen.left(90)

pen.forward(700*2/3) #5th white line from the left
pen.left(90)
pen.forward(500)
pen.left(90)

pen.forward(700) #right side
pen.left(90)
pen.forward(500)
pen.left(90)

pen.forward(700) #right side
pen.left(90)
pen.forward(500)
pen.left(90)

#left goal
pen.left(90)
pen.forward(500/3)
pen.right(90)
pen.forward(700/6)
pen.left(90)
pen.forward(500/3)
pen.left(90)
pen.forward(700/6)


#right goal #width is 700 #height is 500
pen.right(90)
pen.forward(500/3)
pen.right(90)
pen.forward(700) 
pen.right(90)
pen.forward(500/3)
pen.right(90)
pen.forward(700/6)
pen.left(90)
pen.forward(500/3)
pen.left(90)
pen.forward(700/6)
pen.penup()

#draw exit button box and text
button = turtle.Turtle()
button.speed(0)
button.shape("square")
button.color("red")
button.penup()
button.hideturtle()
button.goto(-40, -255)
button.pendown()
button.right(90)
button.forward(33)
button.right(90)
button.forward(50)
button.right(90)
button.forward(33)
button.right(90)
button.forward(50)
button.penup()
button.goto(-63, -283)
button.write("Exit", align="center", font=("Courier", 14, "normal"))

#draw reset button box and text
button.goto(90, -255)
button.color("blue")
button.pendown()
button.right(90)
button.forward(33)
button.right(90)
button.forward(60)
button.right(90)
button.forward(33)
button.right(90)
button.forward(60)
button.penup()
button.goto(63, -283)
button.write("Reset", align="center", font=("Courier", 14, "normal"))

#create P1 goal line
goal1 = turtle.Turtle()
goal1.color("red")
goal1.penup()
goal1.goto(-349,500/6)
goal1.pendown()
goal1.right(90)
goal1.forward(500/3)
goal1.penup()


#create P2 goal line
goal2 = turtle.Turtle()
goal2.color("blue")
goal2.penup()
goal2.goto(349,500/6)
goal2.pendown()
goal2.right(90)
goal2.forward(500/3)

#title
pen.goto(0, 260)
pen.write("Air Hockey", align="center", font=("Courier", 24, "normal"))

#create a ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("pink")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.05
ball.dy = 0.05

# Draw the paddles
paddle_1 = turtle.Turtle()
paddle_1.speed(1000)
paddle_1.shape("circle")
paddle_1.color("red")
paddle_1.penup()
paddle_1.goto(-300,0)
paddle_1.dx = -300
paddle_1.dy = 0

paddle_2 = turtle.Turtle()
paddle_2.speed(1000)
paddle_2.shape("circle")
paddle_2.color("blue")
paddle_2.penup()
paddle_2.goto(300, 0)
paddle_2.dx = 300
paddle_2.dy = 0

# Controlling the paddles on the left with arrow keyboard commands 
def h1():
    paddle_1.forward(10)
 
def h2():
    paddle_1.left(90)
 
def h3():
    paddle_1.right(90)
 
def h4():
    paddle_1.back(10)

wn.onkey(h1, "w")
wn.onkey(h2, "a")
wn.onkey(h3, "d")
wn.onkey(h4, "s")    

# Controlling the paddles on the right with 'wasd' keyboard commands
def k1():
    paddle_2.forward(10)
 
def k2():
    paddle_2.left(90)
 
def k3():
    paddle_2.right(90)
 
def k4():
    paddle_2.back(10)
    
wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")

#function for collision-check
def is_collided_with(a, b):
        return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10

# Create a second turtle called pen2
pen2 = turtle.Turtle()

pen2.speed(0)
pen2.shape("square")
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.pendown()

#function for showing score
def show_score(lftscore,rghtscore):
    pen2.penup()
    pen2.goto(-330,260)
    pen2.pendown()
    pen2.write("P1:      ", align="center", font=("Courier", 15, "normal"))
    pen2.write(lftscore, align="right", font=("Courier", 15, "normal"))
    #P2 score
    pen2.penup()
    pen2.goto(320,260)
    pen2.pendown()
    pen2.write("P2:      ", align="center", font=("Courier", 15, "normal"))
    pen2.write(rghtscore, align="left", font=("Courier", 15, "normal"))
    return lftscore
    return rghtscore

def reset_screen():
    ball.setx(0)
    ball.sety(0)

# reset the game
def reset_game():
    reset_screen()
    lft_score = 0
    rght_score = 0
    pen2.clear()
    show_score(lft_score,rght_score)

# handle screen clicks for buttons
def clickhandler(x, y):
    if x < -40 and x > -90 and y < -255 and y > -288:
        wn.bye()
    elif x < 90 and x > 30 and y < -255 and y > -288:
        reset_game()
        
#setup handler
wn.onscreenclick(clickhandler)

lft_score = 0
rght_score = 0
show_score(lft_score,rght_score)

#Main game loop
while True:
    wn.update()
    wn.listen()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#ball bounces of bounding box
    #Border checking
    #Top Border Check   
    if ball.ycor()>240:
        ball.sety(240)
        ball.dy *= -1

    #Bottom Border Check
    if ball.ycor()<-240:
        ball.sety(-240)
        ball.dy *= -1

    #Right Border Check
    if ball.xcor()>340:
        ball.setx(340)
        ball.dx *= -1

    #Left Border Check
    if ball.xcor()<-340:
        ball.setx(-340)
        ball.dx *= -1

    #goal check
    if ball.ycor() <= (500/6) and ball.ycor() >= (-500/6):
        #left goal
        if ball.xcor() == -340:
            rght_score = rght_score + 1
            pen2.clear()
            show_score(lft_score,rght_score)
            reset_screen()
        #right goal
        if ball.xcor() == 340:
            lft_score = lft_score + 1
            pen2.clear()
            show_score(lft_score,rght_score)
            reset_screen()


    #ball and paddles colliding    
    if is_collided_with(ball,paddle_1) == True or is_collided_with(ball,paddle_2) == True:
        ball.dy *= -1
        ball.dx *= -1



