a = int(input("Enter a number: "))

odd_numbers = []

for i in range(a):
    odd_numbers.append(2 * i + 1)

print(", ".join(map(str, odd_numbers)))
