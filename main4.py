weight= float(input("enter your weight: "))
heigth= float(input("enter your height: "))
bmi=weight/(heigth/100)**2
if bmi<=18.4:
    print("underweight")
elif bmi<=24.9:
    print("healthy")
elif bmi<=29.9:
    print ("overweight")
elif bmi<=34.9:
    print ("obesse")
elif bmi<=39.9:
    print ("severe obesse")
else:
    print ("out of range")
