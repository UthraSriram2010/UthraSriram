def BMI():
    a=float(input("Enter your height in meter:"))
    b=float(input("Enter your weight in kg:"))
    c=a/(b**2)
    if c<=18.5:
        print("You are underweight")
    if c>18.5 and c<=24.9: 
        print("You are correct weight")
    if c>24.9 and c<=29.9:
        print("You are overweight")
    if c>=30:
        print("You are obese")
BMI()
        
        
    
     
    

