burg = input("would you like a burger for $5 (yes/no)")
if burg.strip(" ,.?!@#$%^&*():'").lower() == "yes":
    tcost = 5
fries = input("would you like fries for $3 (yes/no)")
if fries.strip(" ,.?!@#$%^&*():'").lower() == "yes":
    tcost += 3
fcost = tcost * 1.14
print(f"Your total is ${fcost}")