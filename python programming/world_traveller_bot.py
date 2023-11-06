cntr = 0
ccntr = 0
continent = ["Asia", "Europe", "North America", "South America", "Australia", "Africa", "Antarctia"]
name = input("Hello! What's your name?")
print(f"Hello, {name}! It's nice to meet you!")
for _ in range(7):
    cont = input(f"Have you been to {continent[cntr]}?")
    if cont.strip(" ,.?!@#$%^&*():'").lower() == "yes":
        ccntr += 1
    cntr += 1
print(f"I see, you have visited {ccntr}/7 continents!")