# cafe managements

MENU={
    'Pizza':40,
    'Burger':60,
    'Pasta':70,
    'salad':30,
    'Coffee':90,
}

print ("WELCOME TO ARYA RESTURENT")
print("'Pizza':40\n 'Burger':60\n 'Pasta':70\n 'salad':30\n'Coffee':90")

order_total=0

item1=input("Enter the name of item you want to order=")

if item1 in MENU:
    order_total+=MENU[item1]

    print(f"your item{item1}has been added to your order")

else:
    print(f"order item{item1}is not available yet!")    
while True:

    another_order=input("do you want to add another item? (yes/no)") 

    if another_order == "yes":
        item2=input("enter the second item=")
        if item2 in MENU:
           order_total+=MENU[item2]
           print(f"item{item2}has been added to your order")
        else:
            print(f"order item{item2}is not available yet!")
    else:
        print("THANK YOU")        
    print(f"the total amount of item to pay is {order_total}")
    continue
    
        


         

    
    


                    
