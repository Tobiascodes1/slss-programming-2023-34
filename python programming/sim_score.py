p1 = input()
i1 = p1.split()
p2 = input()
i2 = p2.split()

sim_hobbies = 0
for interest in i1:
    if interest in i2:
        sim_hobbies += 1

print(f"you have {sim_hobbies} hobbies in common")