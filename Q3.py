import turtle
import math

length_1 = float(input("What is the length of side 1: "))
length_2 = float(input("What is the length of side 2: "))
angle  = float(input("What is the angle: "))

turtle.forward(length_1)
turtle.right(180 - angle)
turtle.forward(length_2)
angle = math.radians(angle)
side_3 = math.sqrt(((length_1 ** 2) + (length_2 ** 2) - (2 * length_1 * length_2)) * math.cos(angle))
angle_1 = math.asin((side_3 * math.sin(angle)) / length_1)
angle_1 = math.degrees(angle_1)
turtle.right(210 - angle_1)
turtle.forward(side_3)
