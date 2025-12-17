a = int(input("Enter a number: "))

# If a is even, generate odd numbers till (a - 1)
# If a is odd, generate odd numbers till a
limit = a if a % 2 != 0 else a - 1

odd_numbers = []

for i in range(1, limit * 2, 2):
    odd_numbers.append(i)

print(", ".join(map(str, odd_numbers)))
