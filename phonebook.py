
phonebook = []

def menu():
    while True:
        print('СПРАВОЧНИК ГЛАВНОЕ МЕНЮ:'
              '1. Открыть файл'
              '2. Посмотреть все контакты справочника'
              '3. Найти контакт'
              '4. Добавить контакт'
              '5. Выход')
        choice = int(input('Выберите номер пункта меню: '))
        match choice:
            case 1:
                open_file('phone_book\phonebook.txt')
            case 2:
                print_book(phonebook)
            case 3:
                search = input('Введите ключевое слово для поиска: ')
                result = find_contact(search)
                print_book(result)
            case 4:
                pass
            case 5:
                break

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



