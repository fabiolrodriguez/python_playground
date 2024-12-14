weight = input("What is your weight? :")
w_unit = input("(L)bs or (K)g : ")
w_unit = w_unit.upper()

if w_unit == "L":
    converted_weigth = float(weight) * 0.45
    resulted_unit = "Kgs"
elif w_unit == "K":
    converted_weigth = float(weight) / 0.45
    resulted_unit = "Lbs"
else:
    print("Invalid operator")
    exit()

print(f"Your weight is {converted_weigth} {resulted_unit}")
