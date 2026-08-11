from datetime import datetime
try:
    employee_id=input("Employee ID:")
    name=input("Name:")
    basic_salary=int(input("Basic_salary:"))
    allowance=int(input("Allowance:"))
    deduction=int(input("Deduction:"))
    choice=input("If you want all data means yes otherwise no:")
    gross_salary=basic_salary + allowance
    net_salary=gross_salary - deduction
    data=(f"""\nEmployee Id:{employee_id.title()} \n Name:{name.title()} \n Basic Salary:{basic_salary} \n Allowance:{allowance} \n Deduction:{deduction} \n Gross Salary:{gross_salary} \n Net Salary:{net_salary} \n ================================================================== \n """)
    with open("Employee Salary Data.txt",'a') as file:
        file.write(data)
    if choice == 'yes':
        with open("Employee Salary Data.txt",'r') as file:
            print(file.read())
    else:
        print("==========Salary Slip==========")
        print(data)

except  ValueError:
    print("Error:Enter the Valid input")
except:
    print("Error:Something's Wrong")
finally:
    print("=================================================================================")
    print("Thank You")
    x=datetime.now()
    print("=================================================================================")
    print(x)
          
