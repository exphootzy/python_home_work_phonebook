
phonebook = []

def open_file(path):
    global phonebook
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        phonebook.append({'name': contact[0], 'phone': contact[1], 'comment': contact[2]})

def print_book(book: list):
    for contact in book:
        cont = f'{contact["name"]} {contact["phone"]} {contact["comment"]}'
        print(cont)

open_file('phone_book\phonebook.txt')
print_book(phonebook)