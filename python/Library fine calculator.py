from datetime import datetime
print("==========Library Fine Calculator==========")
#inputs
try:
    student_name=input("Enter the student name:")
    if False == student_name.isalpha():
        raise ValueError("Name should be in alphabet")
    
    book=input("Enter the book name:")
    if False == book.isalpha():
        raise ValueError("Book name should be in alphabet")

    due_date=input("Enter the due date(DD-MM-YY):")

    return_date=input("Enter the return date(DD-MM-YY):")
    due_date=datetime.strptime(due_date,"%d-%m-%Y")
    return_date=datetime.strptime(return_date,"%d-%m-%Y")
    days=(return_date - due_date).days

    fine=days * 200

    #Output
    print("==========Library Records==========")    
    with open("Library_record.txt",'a') as file:
        file.write(f"Student Name : {student_name.title()}\n")
        file.write(f"Book Name:{book.title()}\n")
        file.write(f"Due Date:{due_date}\n")
        file.write(f"Return Date:{return_date}\n")
        file.write(f"Fine Amount:{fine}\n")
        file.write("====================================================")
        

    with open("Library_record.txt",'r') as file:
        print(file.read())
        print("\n============================================")
except ValueError as e:
    print("Error:",e)

except:
    print("Somethings Wrong")

finally:
    print("Completed")
