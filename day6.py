#Create an empty tuple
empty_tuple = ()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Lucy", "Amira", "Jennie")
brothers = ("Jake", "Ken", "Emma")

#Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = ("Jude",)
mother = ("Gloria",)
family_members = siblings + father + mother

print(family_members)

#Unpack siblings and parents from family_members
siblings_1, siblings_2, siblings_3, siblings_4, siblings_5, siblings_6, parent_1, parent_2 = family_members

print(siblings_1)
print(siblings_2)
print(siblings_3)
print(siblings_4)
print(siblings_5)
print(siblings_6)
print(parent_1)
print(parent_2)

#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("Banana", "Apple", "Mango")
vegetables = ("Cucumber", "Cabbage", "Carrot")
animal_products = ("Eggs", "Milk", "Cheese", "Butter")

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = len(food_stuff_tp) // 2

if len(food_stuff_tp) % 2 == 0:
    print(food_stuff_tp[middle - 1:middle + 1])
else:
    print(food_stuff_tp[middle])

#Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_tp[:3])
print(food_stuff_tp[-3:])

#Check if an item exists in tuple:
print("Milk" in food_stuff_tp)

#Delete the food_stuff_tp tuple completely
del food_stuff_tp

#Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)

#Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)

