import csv
from datetime import datetime
try:
    Product_details=[['Product_id','Product_name','Price','Quantity'],['P101','Margo',36,20],['P102','Mouse',200,20],['P103','keyboard',350,20]]
    print("""==========Invertory Management System========== \n 1.Add Product \n 2.Display All Products \n 3.Update Stock Quantity \n 4.Search Product \n 5.Show Low Stock Product \n 6.Calculate Total Invertory Value \n 7.Exit""")
    choice=int(input("Enter The Choice(From the menu choose number):"))
    with open("Invertory_data.csv",'w',newline="") as file:
        writer=csv.writer(file)
        print(writer.writerows(Product_details))
    if choice == 1:
        print("==========Add product==========")
        Product_id=input("Enter the Product id:")
        Product_name=input("Enter the Product Name:")
        Price=int(input("Enter the price:"))
        Quantity=int(input("Enter the Quantity:"))
        with open("Invertory_data.csv",'a',newline="") as file:
            writer=csv.writer(file)
            writer.writerow([Product_id,Product_name,Price,Quantity])
    elif choice == 2:
        print("==========Display All products==========")
        with open("Invertory_data.csv",'r') as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                print(row)
    elif choice == 3:
        found=False
        rows=[]
        print("==========Update Stock Quantity==========")
        name=input("Enter the Product_name:").capitalize()
        with open("Invertory_data.csv",'r') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0] !="Product_id":
                    if row[1].lower() == name.lower():
                        row[3]=input("Enter new quantity:")
                        found=True
                rows.append(row)
        with open("Invertory_data.csv",'w',newline="") as file:
            writer=csv.writer(file)
            writer.writerows(rows)
        if found:
            print("Stock Updated Successfully")
        else:
            print("Product Not Found")
    elif choice == 4:
        print("==========Search Product==========")
        found=False
        name=input("Enter the product name:").capitalize()
        with open("Invertory_data.csv",'r') as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if name.lower() == row[1].lower():
                    print("Product_id:",row[0])
                    print("Product_name:",row[1])
                    print("Price:",row[2])
                    print("Quantity:",row[3])
                    found=True
                    break
                if not found:
                    print("Product Not Found")
    elif choice == 5:
        print("==========Low Stock==========")
        found=False
        low_limit=int(input("Enter the low limit of the stock:"))
        with open("Invertory_data.csv",'r') as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if int(row[3]) <= low_limit :
                    print("Product Name:",row[1])
                    print("Quantity",row[3])
                    found=True
                if not found:
                    print("No Low Stock Products")
    elif choice == 6:
        print("==========Total Invertory Value==========")
        total=0
        with open("Invertory_data.csv",'r') as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                total+=int(row[2])*int(row[3])
            print("Total Invertory Value:",total)
    elif choice == 7:
        print("==========Exit==========")
except ValueError:
    print("Error:Enter the valid Input")
except:
    print("Somethings Wrong")
finally:
    print("==========Thank You==========")
    x=datetime.now()
    print(x)
    
            
            
            
                    
                    
        
            
        
        
    
