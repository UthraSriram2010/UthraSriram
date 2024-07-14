students = {}
while True:
    name=input("Enter the student's name(or enter done to finish):")
    if name=='done':
            break
    grade = float(input("Enter the mark:"))


if students:
    avg=sum(students.value())/len(student.value())
    highest=max(students.value())
    lowest=min(students.value())
    
    print(f"Average :{avg}")
    print(f"Highest grades :{highest}")
    print(f"Lowest grades :{lowest}")
            
    for name,grade in students.item():
                print(f"{name};{grade}")
else:
    print("No students data found")
