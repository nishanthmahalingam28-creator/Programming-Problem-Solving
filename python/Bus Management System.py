import csv
from datetime import datetime

try:
    
    seats={1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None,10:None}
    Name=input("Enter The Name:")
    Age=int(input("Enter the Age:"))
    Seat_no=int(input("Enter Seat_no:"))
    Destination={'Coimbatore-chennai':2000,'Coimbatore-Salem':1500,'Coimbatore-Madurai':1200,'Coimbatore-kochin':1200}
    
    for i,j in Destination.items():
        print(i,"\n")
    Destination_choice=input("Enter your trip details:")
    
    for k,l in seats.items():
        
        if Seat_no == k:
            
            if l==None:
                
                print("Seat is available")
                Price=Destination[Destination_choice]
                print("Price:",Price)
                choice=input("Conform to book to your seat(yes or no):")
                
                if choice == 'yes':
                    Seat=Seat_no
                    with open("Bus Management Data.csv",'w') as file:
                        writer=csv.writer(file)
                        writer.writerow(['Passanger','Age','Seat_no','Destination','Price'])
                        writer.writerow([Name,Age,Seat,Destination_choice,Price])
                    print("Successufully booked your seat")
            else:
                print("Seat is not available")
    
except ValueError:
    print("Error:Enter valid input")

except:
    print("Error:Somethings Wrong")

finally:
    print("==========Thank You==========")
    x=datetime.now()
    print(x)
    
