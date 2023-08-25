
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

def add_contact(new):
    global phonebook
    phonebook.append({'name': new[0], 'phone': new[1], 'comment': new[2]})


def menu():
    while True:
        print('СПРАВОЧНИК ГЛАВНОЕ МЕНЮ:\n'
              '\t1. Открыть файл\n'
              '\t2. Посмотреть все контакты справочника\n'
              '\t3. Найти контакт\n'
              '\t4. Добавить контакт\n'
              '\t25. Выход\n')
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
                name = input('Введите имя для нового контакта: ')
                phone = input('Введите номер телефона для нового контакта: ')
                comment = input('Введите комментарий для нового контакта: ')
                add_contact([name, phone, comment])
            case 5:
                break
if __name__ == '__main__':
    menu()