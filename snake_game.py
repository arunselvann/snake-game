import random
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
head.shape("circle")
head.color("pink")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake body
segments = []

def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("pink")
    new_segment.penup()
    segments.append(new_segment)

def move_segment():
    if head.direction != "stop":
        # move the nth segment to n-1th coordinates
        for i in range(len(segments)-1, 0, -1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[i].goto(x, y)

        # move the segment 0 where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
    

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

def move_food():
    if head.distance(food) < 20:
        x = random.randint(-390, 390)
        y = random.randint(-390, 390)
        food.goto(x, y)

        # add a segment
        add_segment()



# Functions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def move_head():
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
    # Check for collision
    if  head.xcor() > 390 or head.xcor() < -390 or head.ycor() > 390 or head.ycor() < -390:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.hideturtle()
        segments.clear()
    move_food()
    move_segment()
    move_head()
    
    time.sleep(delay)

win.mainloop()
