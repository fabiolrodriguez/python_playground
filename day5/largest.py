numbers = [1, 2, 4, 55, 3, 5, 35, 16, 89]
largest = 0
for i in numbers:
    if largest < i:
        largest = i

print(f"The largest number on list is {largest}")