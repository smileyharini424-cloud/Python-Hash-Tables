hash_table = {}


def insert():
    key = input("Enter key: ")
    value = input("Enter value: ")

    hash_table[key] = value

    print("Key-value pair inserted successfully.")


def search():
    key = input("Enter key to search: ")

    if key in hash_table:
        print("Value found:", hash_table[key])
    else:
        print("Key not found.")


def update():
    key = input("Enter key to update: ")

    if key in hash_table:
        value = input("Enter new value: ")
        hash_table[key] = value
        print("Value updated successfully.")
    else:
        print("Key not found.")


def delete():
    key = input("Enter key to delete: ")

    if key in hash_table:
        del hash_table[key]
        print("Key-value pair deleted successfully.")
    else:
        print("Key not found.")


def display():
    if len(hash_table) == 0:
        print("Hash table is empty.")
    else:
        print("Hash Table:")

        for key, value in hash_table.items():
            print(key, ":", value)


while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Update")
    print("4. Delete")
    print("5. Display")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert()

    elif choice == 2:
        search()

    elif choice == 3:
        update()

    elif choice == 4:
        delete()

    elif choice == 5:
        display()

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
