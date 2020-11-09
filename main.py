#Write your code below this row 👇

even_numbers = 0

for num in range(1, 101):
  if num % 2 == 0:
    even_numbers += num

print(even_numbers)

# another solution using the third parameter in range()

total = 0
for num in range(0, 101, 2):
  total += num

print(total)