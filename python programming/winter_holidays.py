import random

ifg = ["I played valorant all day", "I learnd to play league of legends(kinda)", "I got airpods 2"]
ifb = ["I did calculus", "I learned calculus", "I got a bad haircut"]

def winterholiday(good_or_bad):
    if good_or_bad.strip(",;'!@#$%^&*() ").lower() == "good":
        print(random.choice(ifg))
    else:
        print(random.choice(ifb))

def main():
    winterholiday(input("give a summary of your winter holiday"))

if __name__ == "__main__":
    main()