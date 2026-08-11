try:
    def students(name,rollno,total_class,total_class_present):
        print("Name:",name)
        print("Roll no:",rollno)
        print("Total Class:",total_class)
        print("Total Present:",total_class_present)
        percentage=(total_class_present/total_class)*100
        if percentage >= 75:
            print("Attendence:",percentage,"%")
            print("Status:Eligible for exam")
        else:
            print("Attendence:",percentage,"%")
            print("Status:Not eligible for exam")
    name=input("Enter name:")
    if (True != name.isalpha()):
        raise ValueError("Name should contain only alphabets")
    rollno=input("Enter rollno:")
    total_class=int(input("Enter total number of class:"))
    if total_class <0 :
        raise ValueError("Enter the number more than 0")
    total_class_present=int(input("Enter total number of class attended:"))
    if total_class_present <0 :
        raise ValueError("Enter the number more than 0")
    students(name,rollno,total_class,total_class_present)
except ValueError as e:
    print("Error:",e)
finally:
    print("Completed")
