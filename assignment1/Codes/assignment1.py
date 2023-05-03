from fractions import Fraction
import math

ball = int(input("Enter the number of balls : "))
red = int(input("Enter the number of red balls : "))
black = int(input("Enter the number of black balls : "))

while ball != (red+black) :
    red = int(input("Enter the number of red balls : "))
    black = int(input("Enter the number of black balls : "))

answer1 = (math.comb(red,1))*(math.comb(red,1))
answer2 = (math.comb(red,1))*(math.comb(black,1)) + (math.comb(black,1))*(math.comb(red,1))

count = (math.comb(ball,1))*(math.comb(ball,1))

print(f"Question 1 answer = {Fraction(answer1,count)}\nQuestion 2 answer = {Fraction(answer2,count)}\n")