# Создайте программу, хранящую информацию о великих баскетболистах. Нужно хранить ФИО баскетболиста и
# его рост. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте словарь
# для хранения информации.

basketball_players = {}
while True:
    print('1. Добавление баскетболиста')
    print('2. Удаление баскетболиста')
    print('3. Поиск баскетболиста')
    print('4. Замена данных')
    print('5. Выход')

    choice = input('Выберите пункт меню "Великие баскетболисты": ')
    if choice == '1':
        name = input('Введите ФИО великого баскетболиста для добавления: ')
        height = int(input('Введите его рост в см: '))
        basketball_players[name] = {'ФИО': name, 'Рост, см': height}
        print('Информация добавлена! \n')
    elif choice == '2':
        player = input('Введите ФИО баскетболиста для удаления: ')
        if player in basketball_players:
            del basketball_players[player]
            print('Информация удалена! \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '3':
        player = input('Введите ФИО баскетболиста для поиска: ')
        if player in basketball_players:
            print('Информация о баскетолисте:')
            for key, value in basketball_players[player].items():
                print(f'{key}: {value}')
            print(' \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '4':
        player = input('Введите ФИО баскетболиста для замены: ')
        if player in basketball_players:
            name = input('Введите ФИО баскетболиста: ')
            height = int(input('Введите его рост в см: '))
            basketball_players[name] = {'ФИО': name, 'Рост, см': height}
            print('Информация изменена! \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню! \n')

# Создайте программу «Англо-французский словарь». Нужно хранить слово на английском языке и его перевод
# на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных. Используйте
# словарь для хранения информации.

eng_fren_dict = {}

while True:
    print('1. Добавление слова')
    print('2. Удаление слова')
    print('3. Поиск слова')
    print('4. Замена данных')
    print('5. Выход')

    choice = input('Выберите пункт меню «Англо-французский словарь»: ')
    if choice == '1':
        english = input('Введите слово на английском для добавления: ')
        french = input('Введите слово на французком для добавления: ')
        eng_fren_dict[english] = {'Английский': english, 'Французский': french}
        print('Информация добавлена! \n')
    elif choice == '2':
        word = input('Введите слово на английском для удаления: ')
        if word in eng_fren_dict:
            del eng_fren_dict[word]
            print('Информация удалена! \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '3':
        word = input('Введите слово на английском для поиска: ')
        if word in eng_fren_dict:
            print('Информация о слове:')
            for key, value in eng_fren_dict[word].items():
                print(f'{key}: {value}')
            print(' \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '4':
        word = input('Введите слово на английском для замены: ')
        if word in eng_fren_dict:
            english = input('Введите слово на английском для замены: ')
            french = input('Введите слово на французком для замены: ')
            eng_fren_dict[english] = {'Английский': english, 'Французский': french}
            print('Информация изменена! \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню! \n')

# Создайте программу «Фирма». Нужно хранить информацию о человеке: ФИО, телефон, рабочий email,
# название должности, номер кабинета, skype. Требуется реализовать возможность добавления, удаления, поиска,
# замены данных. Используйте словарь для хранения информации.

firm_dict = {}

while True:
    print('1. Добавление')
    print('2. Удаление')
    print('3. Поиск')
    print('4. Замена данных')
    print('5. Выход')

    choice = input('Выберите пункт меню «Фирма»: ')
    if choice == '1':
        fio = input('Введите ФИО для добавления: ')
        phone = input('Введите телефон: ')
        email = input('Введите рабочий email: ')
        post = input('Введите название должности: ')
        office = int(input('Введите номер кабинета: '))
        skype = input('Введите skype: ')
        firm_dict[fio] = {'ФИО': fio, 'Телефон': phone, 'Рабочий email': email, 'Название должности': post,
                          'Номер кабинета': office, 'Skype': skype}
        print('Информация добавлена! \n')
    elif choice == '2':
        fio = input('Введите ФИО для удаления: ')
        if fio in firm_dict:
            del firm_dict[fio]
            print('Информация удалена! \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '3':
        fio = input('Введите ФИО для поиска: ')
        if fio in firm_dict:
            print('Информация о человеке:')
            for key, value in firm_dict[fio].items():
                print(f'{key}: {value}')
            print(' \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '4':
        fio = input('Введите ФИО для замены: ')
        if fio in firm_dict:
            fio = input('Введите ФИО: ')
            phone = input('Введите телефон: ')
            email = input('Введите рабочий email: ')
            post = input('Введите название должности: ')
            office = int(input('Введите номер кабинета: '))
            skype = input('Введите skype: ')
            firm_dict[fio] = {'ФИО': fio, 'Телефон': phone, 'Рабочий email': email, 'Название должности': post,
                              'Номер кабинета': office, 'Skype': skype}
            print('Информация изменена! \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню! \n')

# Создайте программу «Книжная коллекция». Нужно хранить информацию о книгах: автор, название книги,
# жанр, год выпуска, количество страниц, издательство. Требуется реализовать возможность добавления, удаления,
# поиска, замены данных. Используйте словарь для хранения информации.

book_collection = {}

while True:
    print('1. Добавление книги')
    print('2. Удаление книги')
    print('3. Поиск книги')
    print('4. Замена данных')
    print('5. Выход')

    choice = input('Выберите пункт меню «Книжная коллекция»: ')
    if choice == '1':
        name = input('Введите название книги для добавления: ')
        author = input('Введите автора: ')
        genre = input('Введите жанр: ')
        year = int(input('Введите год выпуска: '))
        num_pages = int(input('Введите количество страниц: '))
        publish = input('Введите издательство: ')
        book_collection[name] = {'Название книги': name, 'Автор': author, 'Жанр': genre, 'Год выпуска': year,
                          'Количество страниц': num_pages, 'Издательство': publish}
        print('Информация добавлена! \n')
    elif choice == '2':
        name = input('Введите название книги для удаления: ')
        if name in book_collection:
            del book_collection[name]
            print('Информация удалена! \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '3':
        name = input('Введите название книги для поиска: ')
        if name in book_collection:
            print('Информация о книге:')
            for key, value in book_collection[name].items():
                print(f'{key}: {value}')
            print(' \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '4':
        name = input('Введите название книги для замены: ')
        if name in book_collection:
            name = input('Введите название книги: ')
            author = input('Введите автора: ')
            genre = input('Введите жанр: ')
            year = int(input('Введите год выпуска: '))
            num_pages = int(input('Введите количество страниц: '))
            publish = input('Введите издательство: ')
            book_collection[name] = {'Название книги': name, 'Автор': author, 'Жанр': genre, 'Год выпуска': year,
                          'Количество страниц': num_pages, 'Издательство': publish}
            print('Информация изменена! \n')
        else:
            print('Информация не найдена! \n')
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню! \n')