
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

def find_contact(word: str):
    global phonebook
    result = []
    for contact in phonebook:
        for field in contact.values():
            if word in field:
                result.append(contact)
                break
    return result
open_file('phone_book\phonebook.txt')
print_book(phonebook)

search = input('Введите ключевое слово для поиска: ')
result = find_contact(search)
print_book(result)