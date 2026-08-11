import csv
import os
from datetime import datetime

try:
    class Doctor:
        
        def __init__ (self,name,age,problem):
            self.name=name
            self.age=age
            self.problem=problem
            self.fever=["Dr.K.Kishore","Dr.M.Mohan","Dr.K.Poobalan"]
            self.normal_checkup=["Dr.K.NaveenRaj","Dr.k.Nishanth","Dr.G.Krishan","Dr.S.Sanjay"]
            self.general=["Dr.M.Karthi",'Dr.M.Kathir',"Dr.K.Mohan","Dr.E.Sathish"]
            
            
        def doctor_details(self):
            
            if self.problem == 'fever':
                doctors=self.fever
            elif self.problem == 'normal checkup':
                doctors=self.normal_checkup
            elif self.problem == 'general':
                doctors=self.general
            else:
                print("Sorry,This doctors are not available")

            for i in doctors:
                print(i,'\n')

            select_doctors=input("Select Doctors from above list:")
            Time=input("Enter the time(HH:MM):")
            
            if self.problem == 'fever':
                free_time_doctors_fever={"Dr.K.Kishore":'2:30',"Dr.M.Mohan":'10:30',"Dr.K.Poobalan":'12:30'}
                correct_doctors=free_time_doctors_fever[select_doctors]
                if Time == correct_doctors:
                    print("Doctor is available")
                    choice=input("Conform to appointment(yes or no):")
                    data=[self.name,self.age,self.problem,select_doctors,Time]
                    
                    if choice == 'yes':
                        with open("Hospital_data.csv",'w') as file:
                            writer=csv.writer(file)
                            writer.writerow(['Patient Name','Age','Problem','Doctors','Time'])
                            writer.writerow(data)
                            print("Successfully Appointed")
                    else:
                        print("Visit later")
                            
                else:
                    print("Sorry,Doctor have another appointment.")
                    
            elif self.problem == 'normal checkup':
                free_time_doctors_normal_checkup={"Dr.K.NaveenRaj":'9:00',"Dr.k.Nishanth":'10:45',"Dr.G.Krishan":'12:30',"Dr.S.Sanjay":'2:30'}
                correct_doctors=free_time_doctors_normal_checkup[select_doctors]
                if Time == correct_doctors :
                    print("Doctor is available")
                    choice=input("Conform to appointment(yes or no):")
                    data=[self.name,self.age,self.problem,select_doctors,Time]
                    
                    if choice == 'yes':
                        with open("Hospital_data.csv",'w') as file:
                            writer=csv.writer(file)
                            writer.writerow(['Patient Name','Age','Problem','Doctors','Time'])
                            writer.writerow(data)
                            print("Successfully Appointed")
                    else:
                        print("Visit later")
                else:
                    print("Sorry,Doctor have another appointment.")
                    
            elif self.problem == 'general':
                free_time_doctors_general={"Dr.M.Karthi":'12:30','Dr.M.Kathir':'1:00',"Dr.K.Mohan":'2:30',"Dr.E.Sathish":'3:30'}
                correct_doctors=free_time_doctors_general[select_doctors]
                if Time == correct_doctors :
                    print("Doctor is available")
                    choice=input("Conform to appointment(yes or no):")
                    data=[self.name,self.age,self.problem,select_doctors,Time]
                    
                    if choice == 'yes':
                        with open("Hospital_data.csv",'w') as file:
                            writer=csv.writer(file)
                            writer.writerow(['Patient Name','Age','Problem','Doctors','Time'])
                            writer.writerow(data)
                            print("Successfully Appointed")
                    else:
                        print("Visit later")
                else:
                    print("Sorry,Doctor have another appointment.")
            else:
                print("")
    Name=input("Name:")
    Age=int(input("Age:"))
    Problem=input("Problem:")
    p1=Doctor(Name,Age,Problem)
    p1.doctor_details()
    
except ValueError:
    print("Error:Give Valid Data")

except:
    print("Somethings Wrong")

finally:
    print("================================")
    print("Thank You")
    x=datetime.now()
    print(x)
    print("===============================")
            
                
            
            
            
