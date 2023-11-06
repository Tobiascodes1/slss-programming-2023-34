qnum = 1
rating = 0
fscore = 0
ncourses = int(input("How many courses are you taking?"))
for _ in range(ncourses):
    rating += int(input(f"How would you rate course {qnum} out of 5?"))
    fscore = rating/ncourses
if fscore <= 1:
    print(f"{fscore} ouch")
elif fscore > 1 and fscore < 3:
    print(f"{fscore} Not a bad semester")
elif fscore >= 3:
    print(f"{fscore} Glad to hear that!")