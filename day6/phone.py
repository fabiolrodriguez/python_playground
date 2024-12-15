phone = input("Phone: ")
num_words = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"
}

spelled_phone = ''

for n in phone:
    spelled_phone = spelled_phone + " " + num_words.get(int(n))

print(spelled_phone)