# Shopping cart Program
shopping_cart = []
def add_item(item):
    
    shopping_cart.append(item)
    print(f"The new item is :{item}")

def view_cart():
    if shopping_cart:
        print("Items in shopping cart:")
        for item in shopping_cart:
            print(f"{item}")
        else :
            print("Your cart has no item")

def remove_item():
    if item in shopping_cart:
        shopping_cart.remove(item)
        print(f"{item} in the cart")
    else :
        print(f"{item} not in the shopping_cart")
    
def Shopping_cart_Menu():
    print("Welcome to my shopping cart!")
    print("Make a choice from the below proposition")
    print("1. Add_cart")
    print("2. View_cart")
    print("3. Remove_cart")
    print("4. Exit ")

    # Choose a number from 1 to 4
    choice = int(input("Enter your choice: "))
    if choice == 4:
        print("BYE")
        return 

    if choice == 1:
        item = input("Enter the item:")
        add_item(item)
    elif choice == 2:
         view_cart()
    elif choice == 3:
          item = input("Enter the item:")
          remove_item()
    else:
     print("Invalid choice!")

# Call the function to execute
Shopping_cart_Menu()