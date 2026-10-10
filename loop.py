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
  if i % 2 == 0:
    print(i)
    count += 1

#print all odd numbers be