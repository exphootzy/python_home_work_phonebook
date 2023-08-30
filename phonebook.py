
phonebook = []


def open_file(path):
    global phonebook
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        phonebook.append({'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]})

def save_file(path):
    global phonebook
    result = []
    for contact in phonebook:
        cont = ';'.join(contact.values())
        result.append(cont)
    result = '\n'.join(result)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(result)

def print_book(book: list):
    for contact in book:
        cont = f'{contact["id"]} {contact["name"]} {contact["phone"]} {contact["comment"]}'
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
    phonebook.append({'id': new[0],'name': new[1], 'phone': new[2], 'comment': new[3]})

def delet_contact(id):
    global phonebook
    for contact in phonebook:
        for field in contact.values():
            if (id == field):
                phonebook.remove(contact)
                break
    return phonebook

def edit(c_id: int, contact: list[str]):
    global phonebook
    current_contact = phonebook.get(c_id)
    new_contact = [contact[i] if contact[i] else current_contact[i] for i in range(4)]
    phonebook[c_id] = new_contact 

def menu():
    while True:
        print('СПРАВОЧНИК ГЛАВНОЕ МЕНЮ:\n'
              '\t1. Открыть файл\n'
              '\t2. Сохранить файл\n'
              '\t3. Посмотреть все контакты справочника\n'
              '\t4. Найти контакт\n'
              '\t5. Добавить контакт\n'
              '\t6. Удалить контакт\n'
              '\t7. Изменить контакт\n'
              '\t8. Выход\n')
        choice = int(input('Выберите номер пункта меню: '))
        match choice:
            case 1:
                open_file('phone_book\phonebook.txt')
            case 2:
                save_file('phone_book\phonebook.txt')
            case 3:
                print_book(phonebook)
            case 4:
                search = input('Введите ключевое слово для поиска: ')
                result = find_contact(search)
                print_book(result)
            case 5:
                id = input('Введите уникальный ID для нового контакта: ')
                name = input('Введите имя для нового контакта: ')
                phone = input('Введите номер телефона для нового контакта: ')
                comment = input('Введите комментарий для нового контакта: ')
                add_contact([id, name, phone, comment])
            case 6:
                id = input('Введите уникальный ID для удаления контакта: ')
                result = delet_contact(id)
                print_book(result)
            case 7:
                search = input('Введите ключевое слово для поиска контакта который хотите изменить: ')
                edit_id = input('Введите ID контакта который хотите изменить')
                id = edit_id
                name = input('Введите имя для нового контакта: ')
                phone = input('Введите номер телефона для нового контакта: ')
                comment = input('Введите комментарий для нового контакта: ')
                new_contact = add_contact([id, name, phone, comment])
                edit(edit_id, new_contact)
            case 8:
                break
if __name__ == '__main__':
    menu()