from turtle import Turtle, Screen
import random


def find_turtle(guess):
    if isinstance(guess, str):
        if guess.lower() in rainbow:
            return False
    try:
        guess_num = float(guess)
        if guess_num in rainbow.values():
            return False
    except (TypeError, ValueError):
        pass

    return True

def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

# def get_turtle(guess):
#     if isinstance(guess, str):
#         return guess
#     elif isinstance(guess, (int, float)):
#         return get_key_from_value(rainbow, guess)
def get_turtle(guess):
    if isinstance(guess, str):
        return guess.lower()  # Return lowercase string directly for color name
    elif isinstance(guess, (int, float)):
        return get_key_from_value(rainbow, int(guess))  # Convert to int and get corresponding color name

    return None  # Return None if guess is neither string nor number


def move_turtles():
    finish_line = -240
    while True:
        for turtle in turtles:
            distance = random.randint(0, 20)  # Generate random distance between 0 and 20
            turtle.forward(distance)
            if turtle.xcor() <= finish_line:
                return turtle.color()[0]

screen = Screen()
screen.setup(width=612, height=382)
screen.bgpic("racecourse.gif")

rainbow = {
    "pink": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "cyan": 6,
    "blue": 7,
    "purple": 8
}

turtles = []
y_coord = -133

# Create turtles with colors and initial positions
for color in rainbow:
    tommy = Turtle("turtle")
    tommy.penup()
    tommy.color(color)
    tommy.goto(x=220, y=y_coord)
    y_coord += 38
    tommy.setheading(180)
    turtles.append(tommy)


user_guess = screen.textinput(title="User Guess", prompt="Which turtle do you think will win? Enter color or number:")

while find_turtle(user_guess):
    user_guess = screen.textinput(title="User Guess",
                                  prompt="Invalid input. Enter a color or a number. Which turtle do you think will win?")

winner = move_turtles()
user_winner = get_turtle(user_guess)
if winner == user_winner:
    print(f"The winner is {winner}. You win!")
else:
    print(f"The winner is {winner}. You lose!")

screen.exitonclick()
