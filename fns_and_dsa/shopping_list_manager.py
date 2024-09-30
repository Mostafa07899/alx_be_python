def display_menu():
    print("\nshopping ist manager")
    print("1) add item")
    print("2) remove item")
    print("3) view list")
    print("4) exit")

def add_item(shopping_list):
    item = input("enter the item's name to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the list")

def remove_item(shopping_list):
    item = input("enter the item's name to remove: ")
    if item in shopping_list:
       shopping_list.remove(item)
       print(f"{item} has been removed from the list")
    else:
        print(f"{item} not found in the list")   

def view_list(shopping_list):
    if not shopping_list:
        print("shopping list is empty")
    else:
        print("\n shopping list: ")    
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            pass
        elif choice == '3':
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()    
