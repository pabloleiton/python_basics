# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height**2
round_bmi = round(bmi)
if bmi < 18.5:
    print(f"Your BMI is {round_bmi}, you are underweight.")
else:
    if 18.5 < bmi < 25:
        print(f"Your BMI is {round_bmi}, you have a normal weight.") 
    else:
        if 25 < bmi < 30:
            print(f"Your BMI is {round_bmi}, you are slightly overweight.")
        else:
            if 30 < bmi < 35:
                print(f"Your BMI is {round_bmi}, you are obese.")
            else:
                if 35 < bmi:
                    print(f"Your BMI is {round_bmi}, clinically obese.")