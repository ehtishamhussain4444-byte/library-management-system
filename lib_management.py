print("Press 1 to login in admin profile ")
print("Press 2 to login in user profile ")

stock=[]
borrow=0
def myfuc():
    global borrow,stock
    while True:
        try:
            choice=int(input("Enter ur choice (login in admin or user press 1 or 2)"))
            if choice==0 or choice>=3:
                 print("invalid choice select (1 or 2)")
                 
        except ValueError:
            print("choice must not be string ")
            
        while True:
            if choice==1:
                print("login in admin profile")
                password=input("Enter ur password ").lower()
                if password=="0000":
                    print("Press 1 to add to stock ")
                    print("Press 2 to remove from stock")
                    print("Press 3 to exit from the profile ")
                    try:
                        user=int(input("Enter ur choice for selection (1,2,3):"))
                        if user==0 or user>=4:
                             print("invalid choice")
                    except ValueError:
                        print("input must be integer")

                    if user==1:
                        name=input("Enter the name of book :")
                        try:
                            quantity=int(input("Enter the quantity of books :"))
                        except ValueError:
                            print("value must be integer ")
                        stock.append({name:quantity})
                        print("task is addedd successfully ")

                    elif user==2:
                        
                        name=input("Enter the book name :")
                        global found
                        found=False
                        for x in stock:
                            if name in x:
                                    stock.remove(x)
                                    print("removed successfully")
                                    found=True
                                    break
                            else:
                                print("not found")
                    elif user==3:
                        break
                    else:
                        print("not in option")
                else:
                    print("wronge password ")

            elif choice==2:
                print("u have login in user profile ")
                choose=input("want to borrow or return the book :")

                if choose=="borrow":
                    name=input("enter the name of the book :")
                    try:
                        quantity=int(input("Enter the quantity of a book"))
                    except ValueError:
                        print("value must be integers ")
                        continue
                    
                    
                    for x in stock:
                        if name in x:

                            if quantity <= x[name]:
                                x[name] -= quantity
                                borrow += quantity

                                if x[name] == 0:
                                    stock.remove(x)

                                print("Book borrowed successfully")
                                print("Borrowed books:", borrow)

                            else:
                                print("Not enough books")

                            break

                    else:
                        print("Book not available")
                      
                elif choose=="return":
                    name=input("Enter the book name :")
                    quantity=int(input("Enter the quantity "))
                    stock.append({name:quantity})
                    break
                    
                else:
                    print("invalid choice ")
            else:
                 print("not a valid choice ")
myfuc()

