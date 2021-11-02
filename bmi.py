
while True:

    try:
        user_weight = float(input("Enter you weight in kg "))
    
    except:
        print("Enter valid weight")
        continue
    
    else:
        break


while True:
    
    try:
        user_height = float(input("Enter your height in metre "))
    
    except:
        print("Enter valid height ")
        continue
    
    else:
        break


def calculatebmi(weight,height):
    bmi = weight/height**2
    return bmi
    


print("Your BMI is",calculatebmi(user_weight,user_height),"kg/m2")

bmi = calculatebmi(user_weight,user_height)

if bmi < 18.5:
    print("You are Underweight")

elif bmi >= 18.5 and bmi <25.0:
    print("You are Normal weight")

elif bmi >= 25.0 and bmi < 30.0:
    print("You are Overweight")

elif bmi >= 30.0 and bmi < 35.0:
    print("Obesity class I")

elif bmi >= 35.0 and bmi < 40:
    print("Obesity class II")

elif bmi >=40:
    print("Obesity class III")



