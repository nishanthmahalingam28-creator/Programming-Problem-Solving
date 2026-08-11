try:
    from datetime import datetime
    date=input("Enter the date(DD-MM-YY):")
    Date=datetime.strptime(date,"%d-%m-%Y")
    category=input("Enter the category:")
    description=input("Enter the Description:")
    amount=int(input("Enter the amount:"))
    
    Data=(f"""
           \n ==================================================\n
    Date:{Date.strftime("%D-%m-%Y")}\nCategory:{category.title()}\nDescription:{description.title()}\nAmount:{amount}\n""")
    choice=input("If you want all data means yes:")
    with open("Personal Expense Tracker Data.txt",'a') as file:
        file.write(Data)
    if choice == 'yes':
        total=0
        with open("Personal Expense Tracker Data.txt",'r') as file:
            print(file.read())
            for line in file:
                if line.startswith("Amount"):
                    amount=int(line.split(":")[1])
                    total=total + amount
                    print("=========================================================")
                    print("Total Expense:",total)
    else:
        print(Data)
    print("===============================================================")
    x=datetime.now()
    print(x)
    print("===============================================================")
except ValueError:
    print("Error:Enter the valid input:")
except:
    print("Error:Something Wrong")
finally:
    print("Thank you")
