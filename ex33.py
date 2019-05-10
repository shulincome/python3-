q = 0
numbers = []

for q in range(0, 6):
    print(f"At the top i is {q}")
    numbers.append(q)
    q += 1
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {q}")

print("The numbers")

for num in numbers:
    print(num)


