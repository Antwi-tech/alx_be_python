def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Array to store shopping items

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to shopping list.")
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item not in shopping_list:
                print("Item does not exist")
            else:
                shopping_list.remove(item)
                print("Item has been removed")
        elif choice == 3:
            print("\nYour shopping list:")
            if shopping_list:
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
