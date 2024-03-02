from collections import UserDict


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter the correct user name."
        except IndexError:
            return "Index out of range. Please provide valid input."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact updated."

@input_error
def show_phone(args,contacts):
    try:
        for i in args:
            i=i.capitalize()
            if i in contacts:
                return f'{i}: {contacts[i]}'
    except Exception:
            return "Are you sure? This name doesn\'t exist in contacts"

@input_error
def show_all(args,contacts):
    for name, phone in contacts.items():
        print(name,':',phone)




def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
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
            print(show_phone(args,contacts))
        elif command == "all":
            show_all(args, contacts)
        else:
            print("Invalid command.")


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
if __name__ == "__main__":
    main()