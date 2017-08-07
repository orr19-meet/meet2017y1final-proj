import turtle

import random

turtle.hideturtle()

WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 600 

turtle.penup()

food_list = []
stamp_list = []

food = turtle.clone()
food.shape('circle')

def make_food():
    
    for i in range(3):
        food_x = random.randint(-250,250)
        food_y = random.randint(250,350)
        food_list.append(food_x)
        food.goto(food_x,food_y)
        stamp1 = food.stamp()
        stamp_list.append(stamp1)
        
make_food()





