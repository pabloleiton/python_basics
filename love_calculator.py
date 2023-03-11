# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowname1 = name1.lower()
lowname2 = name2.lower()
plus_lower_names = lowname1 + lowname2

t = plus_lower_names.count("t")
r = plus_lower_names.count("r")
u = plus_lower_names.count("u")
e = plus_lower_names.count("e")

true = t + r + u + e 

l = plus_lower_names.count("l")
o = plus_lower_names.count("o")
v = plus_lower_names.count("v")
e = plus_lower_names.count("e")

love = l + o + v + e

total_love = str(true) + str(love)
total_love_int = int(total_love)

if total_love_int < 10 or total_love_int > 90:
    print(f"Your score is {total_love}, you go together like coke and mentos.")
elif total_love_int < 50 and total_love_int > 40:
    print(f"Your score is {total_love}, you are alright together.") 
else:
    print(f"Your score is {total_love}.")
