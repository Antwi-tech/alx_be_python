def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            item = input("\nEnter item to add: ")
            shopping_list.append(item)
            pass
        elif choice == '2':
            item = input("\nEnter item to remove: ")
            if item not in shopping_list:
                print("Item does not exist")
            else: 
                shopping_list.remove(item)   
                print(f"Item has been removed")
            pass
        elif choice == '3':
            print("\nYour shoping list:\n ")
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()