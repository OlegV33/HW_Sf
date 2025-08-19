import random
# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students: # 1 итерация: student = 'Александра'
      students_marks[student] = {} # 1 итерация: students_marks['Александра'] = {}
      # цикл по предметам
      for class_ in classes: # 1 итерация: class_ = 'Математика'
           marks = [random.randint(1,5) for i in range(3)] # генерируем список из 3х случайных оценок
           students_marks[student][class_] = marks # students_marks['Александра']['Математика'] = [5, 5, 5]
      # выводим получившийся словарь с оценками:
for student in students:
      print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценку ученика по предмету
        5. Исправить оценку ученика по предмету
        6. Удалить ученика. Добавить ученика
        7. Заменить предмет
        8. Вывести все оценки для определенного ученика
        9. Вывести средний балл по каждому предмету для определенного ученика
        10. Вывести средний балл по каждому ученику (Академическая успеваемость')        
        11. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    if command == 4:
        print('4. Удалить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if (student in students_marks.keys() and class_ in students_marks[student].keys()
            and mark in students_marks[student][class_]):
            # удаляем выбранную оценку
            students_marks[student][class_].remove(mark)
            print(f'У {student} по предмету {class_} удалена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика, название предмета или оценка')

    if command == 5:
        print('5. Исправить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # считываем новую оценку
        mark_new = int(input('Введите новую оценку: '))
        # если данные введены верно
        if (student in students_marks.keys() and class_ in students_marks[student].keys()
            and mark in students_marks[student][class_]):
            # удаляем выбранную оценку
            students_marks[student][class_].remove(mark)
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark_new)
            print(f'У {student} по предмету {class_} удалена оценка {mark} '
                  f'добавлена оценка {mark_new}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика, название предмета или оценка')

    if command == 6:
        print('6. Удалить ученика. Добавить ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # Удаляем ученика из словаря
        del students_marks[student]
        # Удаляем ученика из списка
        students.remove(student)
        print('Ученик удален из списка')
        print(students)
        # считываем имя нового ученика
        student_new = input('Введите имя нового ученика: ')
        # Добавляем новго ученика в словарь
        students_marks[student_new] = {}
        # Добавляем новго ученика в список
        students.append(student_new)
        # цикл по предметам
        for class_ in classes:  # 1 итерация: class_ = 'Математика'
            marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
            students_marks[student_new6][class_] = marks
        print('Новый ученик добавлен')
        print(students)

    if command == 7:
        print('7. Заменить предмет')
        # считываем название прежнего предмета
        class_ = input('Введите прежний предмет: ')
        # считываем название нового предмета
        class_new = input('Введите новый предмет: ')
        for student in students:
            # Удаляем прежний предмет из словаря
            del students_marks[student][class_]
            # Добавляем новый предмет в словарь
            students_marks[student][class_new] ={}
        # Удаляем прежний предмет из списка
        classes.remove(class_)
        # Добавляем новый предмет в список
        classes.append(class_new)
        print(f'Предмет {class_} заменен на {class_new}')
        print(classes)

    if command == 8:
        print('8. Вывести все оценки для определенного ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        print(student)
        # цикл по предметам
        for class_ in classes:
            print(f'\t{class_} - {students_marks[student][class_]}')
        print()

    if command == 9:
        print('9. Вывести средний балл по каждому предмету для определенного ученика')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        print(student)
        # цикл по предметам
        for class_ in classes:
            # находим сумму оценок по предмету
            marks_sum = sum(students_marks[student][class_])
            # находим количество оценок по предмету
            marks_count = len(students_marks[student][class_])
            # выводим средний балл по предмету
            print(f'{class_} - {marks_sum // marks_count}')
        print()

    # Расчет академической успеваемости (П.4 Задания)
    elif command == 10:
        print('10. Вывести средний балл по каждому ученику (Академическая успеваемость')
        # цикл по ученикам
        for student in students:
            print(student)
            marks_sum = 0
            marks_count = 0
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum += sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count += len(students_marks[student][class_])
            # выводим средний балл ученика
            print(f'Средний балл - {round(marks_sum / marks_count, 1)}')
            print()


    elif command == 11:
        print('11. Выход из программы')
        break