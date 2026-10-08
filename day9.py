#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age: "))
age_difference = 18 - age

if age >= 18:
  print("You are old enough to drive.")
else:
  print(f"You need {age_difference} more years to learn to drive.")

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 20
your_age = int(input("Enter your age: "))
age_diff = abs(my_age - your_age)

if my_age > your_age:
    if age_diff == 1:
        print(f"I am {age_diff} year older than you")
    else:
        print(f"I am {age_diff} years older than you")
else:
    if age_diff == 0:
        print("We are age mates")
    elif age_diff == 1:
        print(f"You're {age_diff} year older than me")
    else:
        print(f"You're {age_diff} years older than me")

#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
  print(f"{a} is greater than {b}")
elif a < b:
  print(f"{a} is smaller than {b}")
else:
  print(f"{a} equals {b}")


#Write a code which gives grade to students according to theirs scores:
score = float(input("Enter student score: "))

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")
else:
  print("Grade: F")

#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
winter = ["December", "January", "February"]
autumn = ["September", "October", "November"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]
month = str(input("Enter month: "))

if month in autumn:
  print("The season is Autumn")
elif month in spring:
  print("The season is Spring")
elif month in winter:
  print("The season is Winter")
elif month in summer:
  print("The season is Summer")
else:
  print("Enter a valid month")

#The following list contains some fruits:
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input("Enter a fruit: "))

if fruit not in fruits:
  fruits.append(fruit)
  print(fruits)
else:
  print('That fruit already exist in the list')


#Here we have a person dictionary. Feel free to modify it!
person = {
  'first_name': 'Asabeneh',
  'last_name': 'Yetayeh',
  'age': 250,
  'country': 'Finland',
  'is_married': True,
  'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  'address': {
    'street': 'Space street',
    'zipcode': '02210'
  }
}
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    middle = len(person["skills"]) // 2

    if len(person["skills"]) % 2 == 0:
        print(person["skills"][middle - 1:middle + 1])
    else:
        print(person["skills"][middle])
else:
    print("skill not in dictionary")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person:
  if "Python" in person["skills"]:
    print("person has Python skills")
  else:
    print("person doesn't have Python skills")
else:
  print("skill not in dictionary")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if set(person["skills"]) == {"JavaScript", "React"}:
    print("He is a front end developer")
elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
    print("He is a backend developer")
elif "React" in person["skills"] and "Node" in person["skills"] and "MongoDB" in person["skills"]:
    print("He is a fullstack developer")
else:
    print("unknown title")


#If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
if person["is_married"] and person["country"] == "Finland":
    print(f'{person["first_name"]} {person["last_name"]} lives in Finland. He is married.')