try:
    from datetime import datetime
    customer_name=input("Enter Customer Name:")
    Customer_name=customer_name.lower().capitalize()
    if False == Customer_name.isalpha() :
        raise ValueError("Name should be alphabet:")
    service_no=input("Enter Service NO:")
    units=int(input("Enter The Units:"))
    if 0 <=  units <=100:
        Energy_charge=units*1.5
    elif 101 <= units <=200:
        Energy_charge=100*1.5 +(units-100)*2.5
    elif 201 <= units <=300:
        Energy_charge=(100*1.5 )+(100*2.5)+(units-200)*4
    elif 301<= units <=500:
        Energy_charge=(100*1.5)+(100*2.5)+(100*4)+(units-300)*6
    Fixed_charge=50
    Total_amount=Energy_charge+Fixed_charge
    with open("Electricity bill Data.txt",'a') as file:
        file.write(f"Customer Name:{Customer_name.title()}\n")
        file.write(f"Service No:{service_no.title()}\n")
        file.write(f"Units:{units}\n")
        file.write(f"Energy charge:{Energy_charge}\n")
        file.write(f"Fixed_charge:{Fixed_charge}\n")
        file.write(f"Total_amount:{Total_amount}\n")
        file.write("=========================================\n")
    bills=input("If you want all bills means yes:")
    print("=============Electricity Bill========================\n")
   
    if bills =='yes':
        with open("Electricity bill data.txt",'r') as file:
            print(file.read())
    else:
        print("Customer Name:",Customer_name)
        print("\nService No:",service_no)
        print("\nUnits:",units)
        print("\nEnergy charge:",Energy_charge)
        print("\nFixed charge:",Fixed_charge)
        print("\nTotal Amount:",Total_amount)
    print("=======================================================\n")
    x=datetime.now()
    print(x)
except ValueError as e:
    print("Error:",e)
except:
    print("Somethings Wrong")
finally:
    print("Thank You")
