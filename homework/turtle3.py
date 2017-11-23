from turtle import *

def draw_square(lenght, color):
    pencolor(color)
    for i in range(4):
        forward(lenght)
        left(90)
    mainloop()

length_ = int(input("Enter length: "))
color_ = input("Enter pen color: ")

draw_square(length_, color_)
