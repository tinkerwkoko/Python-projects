import math
#Declare your age as integer variable
age = 26

#Declare your height as a float variable
height = 1.72

#Declare a variable that store a complex number
comp = 2 + 3j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print(area_of_triangle)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter_of_triangle = a + b + c
print(perimeter_of_triangle)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)

print(area_of_rectangle)
print(perimeter_of_rectangle)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter radius of circle: "))
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
#Compare the slopes in tasks 8 and 9.
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
#There is no 'on' in both dragon and python
#Find the length of the text python and convert the value to float and convert it to string
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
#Check if type of '10' is equal to type of 10
#Check if int('9.8') is equal to 10
#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?