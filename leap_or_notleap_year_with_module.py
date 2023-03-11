# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if int(year) % 4 != 0:
    print("Not leap year.")
else:
    if int(year) % 100 != 0:
        print("Leap year.")
    else:
        if int(year) % 400 == 0:
            print ("Leap year.")
        else:
            print ("Not leap year")