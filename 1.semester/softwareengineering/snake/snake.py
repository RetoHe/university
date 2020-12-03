#https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900

import turtle
import time
import random

delay = 0.1

# Score einrichten
score = 0
high_score = 0

#user_input = turtle.Screen()
#user_input.bgcolor("blue")
#user_input.setup(width=300, height=300)
#user_input
#user = user_input.textinput("Herzlich Willkommen zu unserem Snake ", "Bitte geben Sie Ihren Nutzernamen ein:")

# Snake Bildschirm
wn = turtle.Screen()
wn.title("Snake by Louis, Tobias und Reto DSIA19")
wn.bgcolor("grey")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates
user = wn.textinput("Herzlich Willkommen zu unserem Snake ", "Bitte geben Sie Ihren Nutzernamen ein:")
# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("User: {} Score: 0  High Score: 0".format(str(user)), align="center", font=("Courier", 24, "normal"))


# Functions
def go_up():
    if head.direction != "down":   #sofortige Richtungswechsel um 180 Grad sind dadurch nicht möglich
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
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


# Tastatur Einstellungen
wn.listen()
wn.onkeypress(go_up, "w")  # w für nach oben
wn.onkeypress(go_down, "s") # s für nach unten
wn.onkeypress(go_left, "a") # a für nach links
wn.onkeypress(go_right, "d") # d für nach rechts

# Game Schleife
while True:
    wn.update()

    # Check ob Snake mit der Abgrenzung kollidiert
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Segmente verstecken, da wir es nicht schaffen die einzelnen Segmente zu löschen
        for segment in segments:
            segment.goto(1000, 1000)

        # Löschen der Segmente
        segments.clear()

        # Reset score
        score = 0

        # Reset Zeitverzögerung
        delay = 0.1

        pen.clear()
        pen.write("User: {}  Score: {}  High Score: {}".format(str(user), score, high_score), align="center", font=("Courier", 24, "normal"))

        # Check ob Snake mit dem Futter kollidiert
    if head.distance(food) < 20:
        # neues Futterstück zufälllig verteilen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Snake vergrößern
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Verkürzen Zeitverzögerung
        delay -= 0.001

        # Score erhöhen
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("User: {}  Score: {}  High Score: {}".format(str(user), score, high_score), align="center", font=("Courier", 24, "normal"))

        # Anordnen der Elemente in verdrehter Reihenfolge
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # erstes Segment wird mit Snake Head verbunden
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check ob Snake mit dem Snake Body kollidiert
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Segmente verstecken, da wir es nicht schaffen die einzelnen Segmente zu löschen
            for segment in segments:
                segment.goto(1000, 1000)

            # Löschen der Elemente
            segments.clear()

            # Reset score
            score = 0

            # Reset Zeitverzögerung
            delay = 0.1

            # Aktualisieren des Score Boards
            pen.clear()
            pen.write("User: {}  Score: {}  High Score: {}".format(str(user), score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()