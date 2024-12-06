import math

price = 1000000
good_credit = False

if good_credit:
    price = price - ((price*10)/100)
else:
    price = price - ((price*20)/100)

print(f"The payment should be ${price}")
