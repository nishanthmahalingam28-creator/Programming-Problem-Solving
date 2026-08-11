from datetime import datetime
#Account details

pin=2081

balance=50000

#input
try:
    for i in range(0,3,1):
        Pin=int(input("Enter your pin:"))

        #Check pin is correct or not

        if(Pin == pin):
            print("Your Pin is correct\n")
            print("Withdrawal \t Deposit \t Check balance \t Transaction history \t Exit \n")
            choice1=input("Enter your choice:")
            choice=choice1.lower().capitalize()
            
            if choice == 'Withdrawal' :

                print("Balance:",balance)
                withdraw=int(input("Enter the withdrawal amount:"))
                if withdraw <= balance:
                    print("Amount successfully Withdrawed \n Please collect your cash")
                    print("Balance:",balance-withdraw)
                else:
                    print("Balance is insufficient")
                    print("Balance:",balance)
                break

            elif (choice == 'Deposit'):
                deposit=int(input("Enter deposit Amount:"))
                balance=balance+deposit
                print("Successfully deposited \n Balance:",balance)
                break

            elif (choice == 'Check balance'):
                print("Balance:",balance)
                break

            else:
                break

        else:
            print("Pin is incorrect")

    else:
        print("Attempted failed Try after few hours")

except ValueError as e:
    print("Error:",e)

except:
    print("Somethings Wrong")
finally:
    print("Thank you for using ATM Machine")
    x=datetime.now()
    print(x)

    
                     
            
            
