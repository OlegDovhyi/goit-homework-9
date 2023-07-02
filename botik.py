contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid command."
    return inner

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Added contact: {name}, {phone}"

@input_error
def change_phone(name, phone):
    contacts[name] = phone
    return f"Changed phone number for contact: {name}, {phone}"

@input_error
def get_phone(name):
    return contacts[name]

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    else:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()

def main():
    print("How can I help you?")
    
    while True:
        command = input("> ").lower()
        
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            try:
                _, name, phone = command.split()
                print(add_contact(name, phone))
            except ValueError:
                print("Enter name and phone number, separated by a space.")
        elif command.startswith("change"):
            try:
                _, name, phone = command.split()
                print(change_phone(name, phone))
            except ValueError:
                print("Enter name and new phone number, separated by a space.")
        elif command.startswith("phone"):
            try:
                _, name = command.split()
                print(get_phone(name))
            except ValueError:
                print("Enter a name.")
        elif command == "show all":
            print(show_all_contacts())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
