#   Функція для розбору вводу користувача на команду та аргументи.
def parse_input(user_input): 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


 # Функція для додавання нового контакту.
def add_contact(args, contacts):
    
    if len(args) != 2:
        return "Invalid command. Please provide both name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Функція для зміни номера телефону існуючого контакту.
def change_contact(args, contacts):
   
    if len(args) != 2:
        return "Invalid command. Please provide both name and new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

# Функція для показу номера телефону за ім'ям.
def show_phone(args, contacts):
    
    if len(args) != 1:
        return "Invalid command. Please provide a name."
    name = args[0]
    if name in contacts:
        return f"The phone number of {name} is {contacts[name]}."
    else:
        return "Contact not found."

# Функція для показу всіх контактів.
def show_all(contacts):
 
    if not contacts:
        return "No contacts found."
    contact_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return contact_list


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
