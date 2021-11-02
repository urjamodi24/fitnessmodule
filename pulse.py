print("Place the tips of your index, second and third fingers on the palm side of your other wrist below the base of the thumb. Or, place the tips of your index and second fingers on your lower neck on either side of your windpipePress lightly with your fingers until you feel the blood pulsing beneath your fingers. You may need to move your fingers around slightly up or down until you feel the pulsing.Use a watch with a second hand, or look at a clock with a second hand.Count the beats you feel for 10 seconds. Multiply this number by six to get your heart rate (pulse) per minute.")

while True:

    try:
        age = int(input("Enter your age in years - "))
    
    except:
        print("Enter valid age")
        continue
    
    else:
        break


while True:

    try:
        pulse = int(input("Enter your pulse in bpm - "))
    
    except:
        print("Enter valid pulse")
        continue
    
    else:
        break


max_heart_rate= int(220-age)
print("maximum heart rate is this-",max_heart_rate)

min_target = (65/100)*max_heart_rate
max_target =(85/100)*max_heart_rate

if pulse >=min_target and pulse <= max_target:
    print("You are exercising well keep going!!")
elif pulse >max_target and pulse <= max_heart_rate:
    print("Slow down your target heart rate should in between",min_target,"and",max_target)
elif  pulse > max_heart_rate:
    print("Stop your target heart rate should in between",min_target,"and",max_target)
elif pulse < min_target :
    print(" Exercise harder your target heart rate should in between",min_target,"and",max_target)
    
    

    



