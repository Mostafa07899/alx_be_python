def display_menu():
    print("Shopping List Manager")
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
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()    
