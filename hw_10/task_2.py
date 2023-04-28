import json

phonebook = dict()


def greeting_command() -> None:
    GREETING_TEXT = """Welcome to the Phonebook application!"""
    print(GREETING_TEXT)
    load_phonebook()
    print("Enter a task type from the list: add contact, search, delete contact, update contact, quit")
    command = input("Enter: ")
    if command == "add contact":
        add_contact()
        save_phonebook()
    elif command == "search":
        search_contact()
    elif command == "delete contact":
        delete_contact()
        save_phonebook()
    elif command == "update contact":
        update_contact()
        save_phonebook()
    elif command == "quit":
        print("The Phonebook application is closed")
    else:
        print("An invalid command was entered. Please enter the command again.")
        greeting_command()


def load_phonebook() -> None:
    try:
        with open('phonebook.json') as file:
            phonebook.update(json.load(file))
    except FileNotFoundError:
        print("File not found")


def save_phonebook() -> None:
    with open('phonebook.json', 'w') as file:
        json.dump(phonebook, file)


def add_contact() -> None:
    name = input("Enter name: ")
    last_name = input("Enter last name: ")
    full_name = name + " " + last_name
    phone_number = input("Enter your phone number: ")
    city = input("Enter a city: ")
    phonebook[phone_number] = {
        "name": name,
        "last name": last_name,
        "full name": full_name,
        "phone number": phone_number,
        "city": city,
    }
    print("Entry added")


def search_contact() -> None:
    search_type = input("Enter the type of search: name, last name, full name, phone number, city: ")
    search_dict = {
        "name": "Enter name: ",
        "last name": "Enter last name: ",
        "full name": "Enter full name: ",
        "phone number": "Enter your phone number: ",
        "city": "Enter a city: ",
    }
    for key in search_dict.keys():
        if search_type == key:
            type = input(search_dict[key])
            results = [entry for entry in phonebook.values() if entry[key] == type]
            break
        else:
            print("Incorrect search type")
            return search_contact()
    print("Search Results: ")
    for result in results:
        print(result)


def delete_contact() -> None:
    phone_number = input("Enter the phone number of the contact you want to delete: ")
    if phone_number in phonebook:
        del phonebook[phone_number]
        print("Contact deleted")
    else:
        print("No contact found")


def update_contact() -> None:
    phone_number = input("Enter the phone number of the contact you want to update: ")
    if phone_number in phonebook:
        contact = phonebook[phone_number]
        field = input("Enter the field you want to update: name, last name, phone number, city: ")
        value = input("Enter the new value: ")
        contact[field] = value
        print("Contact updated")
    else:
        print("No contact found")


greeting_command()