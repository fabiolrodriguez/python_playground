numbers = [5, 2, 1, 7, 4]
numbers.remove(2)
numbers.append(11)

i = 0
for i in range(10):
    numbers.append(i)
    i += i

print(numbers)

print(numbers.index(5))

print(numbers.count(5))

ordered_numbers = numbers.copy()

ordered_numbers.sort()

print(ordered_numbers)

numbers.clear()

print(numbers)