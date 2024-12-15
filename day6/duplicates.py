numbers = [3, 6, 7, 2, 3 ,6 ,7]

for i in range(10):
    numbers.append(i)

print(f"Raw List{numbers}")

for n in numbers:
    while numbers.count(n) > 1:
        numbers.remove(n)


print(f"No duplicates List{numbers}")