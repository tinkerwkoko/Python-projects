#Create an empty dictionary called dog
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog = {"Name": "Bimgo", "Color": "Red", "Breed": "Ekuke", "Legs": 4, "Age": 2}
print(dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
  "first_name": "Kosi",
  "last_name": "Amams",
  "gender": "Female",
  "age": 25,
  "marital_status": "Single",
  "Skills":['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
  "country": "Nigeria",
  "city": "Lagos",
  "address": "Ikotun"
  }

#Get the length of the student dictionary
print(len(student))

#Get the value of skills and check the data type, it should be a list
print(student.get("Skills"))
print(type("Skills"))

#Modify the skills values by adding one or two skills
student["Skills"].append("HTML")
print(student)

#Get the dictionary keys as a list
student_keys = student.keys()

#Get the dictionary values as a list
student_values = student.values()

#Change the dictionary to a list of tuples using items() method
new_student = tuple(student)
print(new_student)

#Delete one of the items in the dictionary

#Delete one of the dictionaries
del student