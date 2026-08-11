try:
    import datetime
    x=datetime.datetime.now()
    print("=======Items are Available=======")
    items={
        "Tea":15,
        "Coffee":20,
        "Burger":50,
        "Samosa":10,
        "Sweet 1KG":60,
        "Biscuit":10,
        "Juice":10
    }
    len_items=0
    len_price=0
    for i in items.keys():
        if len_items<len(i):
            len_items=len(i)
    print("Items And Price list")
    for item,Price in items.items():
        print("|",' '*(len_items-len(item)),item,"|",Price,"|")
    #input
    customer_name=input("Enter Customer Name:")
    if False == customer_name.isalpha():
        raise ValueError("Name should be alphabets")
    input_item={}
    while True:
        item_1=input("Select item:")
        item_2=item_1.lower().capitalize()
        if item_2 not in items:
            raise ValueError("Item is wrong Please Check the menu")
        quantity=int(input("Quantity of item:"))
        input_item[item_2]=quantity

        add=input("Add more items(yes or no):")
        if add == 'no':
            break
    print("===========Billing System==========")
    print("Customer name:",customer_name.lower().capitalize())
    total_cost=0
    for i,j in input_item.items():
        print(i,"*",j,"= Rs.",items[i]*j)
        total_cost=total_cost+items[i]*j
        print("Total cost:",total_cost)
        if total_cost >= 200:
            Discount=total_cost*0.1
        else:
            Discount=0
    print("Discount:",Discount)
    print("Final price:",total_cost - Discount)
    print("=====================================")
    print(x)
    print(x.strftime("%A"))
except ValueError as e:
    print("Error:",e)
finally:
    print("Completed")

