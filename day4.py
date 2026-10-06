#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
sentence = ['Thirty', 'Days', 'Of', 'Python']
full_sentence = ' '.join(sentence)
print(full_sentence)

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
conca = ['Coding', 'For' , 'All']
result = ' '.join(conca)
print(result)

#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
company_slice = company[:6]
print(company_slice)

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

#Change "Python for Everyone" to "Python for All" using the replace method or other methods.
my_word = "Python for Everyone"
print(my_word.replace("Everyone", "All"))

#Split the string 'Coding For All' using space as the separator (split()) .
print(company.split( ))

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

#What is the character at index 0 in the string Coding For All.
print(company[0])

#What is the last index of the string Coding For All.
print(company[-1])

#What character is at index 10 in "Coding For All" string.
print(company[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.


#Create an acronym or an abbreviation for the name 'Coding For All'.


#Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new_sentence = 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.index("because"))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.rfind("because"))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence[31:54])

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_sentence.find("because"))

#Does 'Coding For All' start with a substring Coding?
print(company.find("Coding"))

#Does 'Coding For All' end with a substring coding?
print(company.rfind("Coding"))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
company_2 = '   Coding For All      '  
print(company_2.strip( ))

#Which one of the following variables return True when we use the method isidentifier():
sentence_1= "30DaysOfPython"
sentence_2 = "thirty_days_of_python"
print(sentence_1.isidentifier())
print(sentence_2.isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
py_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(py_libraries))

#Use the new line escape sequence to separate the following sentences. I am enjoying this challenge. I just wonder what is next.
print("I\nam\nenjoying\nthis\nchallenge.")
print("I\njust\nwonder\nwhat\nis\nnext.")
#Use a tab escape sequence to write the following lines.
#Use the string formatting method to display the following:

