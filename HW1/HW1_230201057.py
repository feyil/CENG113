#230201057

age=input("Please type your age:")
gender=(raw_input("Please type your gender(woman or man):")).lower() #case insensitive
height=input("Please type your height in centimetre(ex.:177):")#height(cm)
weight=input("Please type your weight in kilogram(ex.:80):")#weight(kg)
if 0<age<30:
    if gender=="woman":
        n=5
        m=-161
        calfor=10*weight+6.25*height-n*age+m #calculation to stay in the same weight
        print "Calorie per day:",calfor
    elif gender=="man":
        n=5
        m=5
        calfor=10*weight+6.25*height-n*age+m #calculation to stay in the same weight
        print "Calorie per day:",calfor
    else:
         print "You typed invalid value for gender. Please try again."
elif age>=30:
    if gender=="woman":
        n=7
        m=-161
        calfor=10*weight+6.25*height-n*age+m #calculation to stay in the same weight
        print "Calorie per day:",calfor
    elif gender=="man":
        n=7
        m=5
        calfor=10*weight+6.25*height-n*age+m #calculation to stay in the same weight
        print "Calorie per day:",calfor
    else:
         print "You typed invalid value for gender. Please try again."
else:
    print "You typed invalid value for age. Please try again."