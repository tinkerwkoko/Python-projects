#print all numbers from 1-10 using a loop
for i in range(1, 11):
  print(i)

count = 1

while count <= 10:
  print(count)
  count += 1

#print numbers from 10 down to 1 in reverse order
for i in range(10, 0, -1):
  print(i)

count = 10
while count >= 1:
  print(count)
  count -= 1

#print all even numbers between 1 and 100
for i in range(101):
  if i % 2 == 0:
    print(i)

count = 0

while count <= 100:
  if count % 2 == 0:
    print(count)
  count += 1

#print all odd numbers between  1 and 100
for i in range(101):
  if i % 2 == 1:
    print(i)

count = 0

while count <= 100:
  if count % 2 == 1:
    print(count)
  count += 1

#5 print the multiplication table of a given number from n * 1 to n * 10
n = int(input("Enter a number: "))

for i in range(1, 11):
  print(f"{n} * {i} = {n * i}")

n = int(input("Enter a number: "))
i = 1

while i <= 10:
  print(f"{n} * {i} = {n * i}")
  i += 1

#6 calculate and print the sum of the first n natural numbers
n = int(input("Enter a number: "))

numbers =[]
for i in range(1, n+1):
  numbers.append(i)

total = sum(numbers)
print(total)