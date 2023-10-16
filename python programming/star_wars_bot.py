# Star Wars Bot
# Author: Toby Ma
# October 16, 2023


yes = ["yes","yeah","yup","yea","ya","correct","affirmative"]
ds = 0

print("hello, I am Star Wars Bot, I wil decide if you are in the light side or the the dark side")
print("through two questions, I can predict if you will fall to the dark side or stay on the light side")
print("now, let us begin with the first question... do you like the color red")
r1 = input()
if r1.lower().strip("!,.? ") in yes:
    print("hmmm, interesting")
    ds = 1
print("second question, do you like capes?")
r2 = input()
if r2.lower().strip("!,.? ") in yes:
    ds = 1
    print("very interesting indeed")
if ds == 1:
    print("the dark side is strong with this one")
    print("side question, have you heard of the tale of darth plageius the wise?")
elif ds == 0:
    print("k I think you're probably a jedi")