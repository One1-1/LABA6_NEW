"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызов запрашивает нужные исходные данные подпрограммы
"""

from lab6.my_library import task6_1, line40


def menu():
    """
    Функция предлагает выбор номера задания и номера лабораторной работы\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
             choice_lab - выбранный номер лабы
    """
    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()
        print('программа запустилась, посмотрите файлы')


        match choice:

            case 1:
                task6_1(way='lab6/name/files')

            case 2:

                line40('lab6/name/input.txt', 'lab6/name/output.txt')



            case _:
                break

        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

