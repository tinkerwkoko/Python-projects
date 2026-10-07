it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
companies_2 = {"Paystack", "Paypal", "Meta"}
it_companies.update(companies_2)
print(it_companies)

#Remove one of the companies from the set it_companies
print(it_companies.pop())

#What is the difference between remove and discard
#remove throws an error if the item is not found
#discard doesn't

#Join A and B
C = A | B
print(C)
#Find A intersection B
D = A & B
print(D)

#Is A subset of B
A.issubset(B)

#Are A and B disjoint sets
A.isdisjoint(B)

#Join A with B and B with A
F = A | B & B |A
print(F)

#What is the symmetric difference between A and B
G = A ^ B
print(G)

#Delete the sets completely
del A
del B

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
new_age = set(age)
print(new_age)

print(len(age) > len(new_age))

#Explain the difference between the following data types: string, list, tuple and set
#strings are texts enclosed in single, double or triple quotes
#lists are mutable and ordered datatype in python. represented by square brackets
#tuples are immutable and ordered datatype in python. represented by brackets
#sets are mutable and unordered datatype in python. represented with curly braces

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
word = "I am a teacher and I love to inspire and teach people."
words = word.split()
unique_words = set(words)
print(unique_words)