import turtle
import time

delay = 0.2

win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("blue")
win.setup(width=800, height=800)
win.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("pink")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# keyboard bindings
win.listen()
win.onkeypress(go_up, 'Up')
win.onkeypress(go_down, 'Down')
win.onkeypress(go_left, 'Left')
win.onkeypress(go_right, 'Right')
# Main game loop
while True:
    win.update()

    move()
    time.sleep(delay)

win.mainloop()
