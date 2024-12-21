import turtle
import time
import random

WIDTH , HEIGHT = 600,600
COLORS= ['red' , 'green', "blue" ,'cyan' , 'pink' , 'gray' , "black" , 'yellow' , 'orange' , 'purple' ]


MIN_RACER=2
MAX_RACER=10


def get_number_of_racers():
    
    while True:
        racer=input("Enter the Number of racers (2-10):-  ") 
        if racer.isdigit():
            racer=int(racer)
            if MIN_RACER <= racer <= MAX_RACER:
                break
            else:
                print("enter Valid number of racers")
        else:
            print("invalid! Enter in Number")
    return racer

def race(colors):
    turtles=create_turtle(colors)
    while True:
        for racer in turtles:
            distance= random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>=HEIGHT//2 -10:
                return colors[turtles.index(racer)]



def create_turtle(colors):
    turtles=[]
    spacingx=WIDTH //(len(colors)+1)
    for i , color in enumerate(colors):
        racers= turtle.Turtle()
        racers.color(color)
        racers.shape("turtle")
        racers.left(90)
        racers.penup()
        racers.setpos(-WIDTH//2 + (i+1) *spacingx , -HEIGHT//2 + 20 )
        racers.pendown
        turtles.append(racers)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH , HEIGHT)
    screen.title("Turtle Racing Game!")


num_racer=get_number_of_racers()
init_turtle()
    
random.shuffle(COLORS)
colors=COLORS[:num_racer]

winner=race(colors)
print(f"The Winner is The turtle with color: - {winner}")

time.sleep(5)

input("press q to quit")
