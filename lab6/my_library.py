import os

def task6_1(way):
    '''
    Задание:
    Дан файл, содержащий целые числа. Описать логическую функцию, проверяющую,
    упорядочены ли по возрастанию элементы непустого файла. Если да, записать данные
    в новый файл в обратном порядке, иначе записать максимальное и минимальное
    значения. Предусмотреть обработку всех возможных исключительных ситуаций

    :param way: путь к файлу
    :return: None
    '''

    f = open(way, encoding='utf-8')                     #открытие файла с кодировкой utf-8
    text = list(map(int, f.read().split()))             #преобразование в список чисел
    max = 0                                             #для определения возрастания последовательности
    flag = False                                        #для определения возрастания последовательности
    text_revers = list(reversed(text))                  #обратный порядок


    #Функция для возрастающей последовательности
    def create_new_file_for_increasing(text_revers):
        '''
        Процедура записывает в обратном порядке строку

        :param text_revers: числа в обратном порядке
        :return: None
        '''
        new_file = open('lab6/name/new', 'w+')
        for num in text_revers:
            new_file.write(str(num) + ' ')
        new_file.close()


    #Функция для убывающей последовательности
    def create_new_file_for_descending(text):
        '''
        Процедура записиывает в файл максимальное и минимальное значение исходного файла

        :param text: числа из исходного файла
        :return: None
        '''
        new_file = open('lab6/name/new', 'w+')
        new_file.write(str(text[len(text)-1]) + ' ' + str(text[0]))
        new_file.close()


    #Проверка, пустой файл или нет, если не пустой, то начать выполнение основной программы
    if os.path.isfile(way):
        print("Файл существует")

        for i in text:

            if i >= max:
                max = i
                flag = True

            else:
                flag = False
                break


        #если последовательность возрастает
        if flag == True:
            create_new_file_for_increasing(text_revers)
            print('Файл записан')


        #если последовательность убывает
        else:
            create_new_file_for_descending(text)
            print('Файл записан')


    else:
        print("Файл не существует")






def line40(f, t):
    '''
    Задание:
    Описать процедуру line40(f, t), которая считывает из файла f литеры до первой точки
    и записывает их (без точки) в текстовый файл t, формируя в нем строки по 40 литер (в
    последней строке может быть и меньше). Предусмотреть обработку всех возможных
    исключительных ситуаций.

    :param f: файл для чтения
    :param t: файл для записи
    :return: None
    '''

    print('Запсук')
    infile = open(f, 'r', encoding='utf-8')   #Открываем файл для чтения
    outfile = open(t, 'w', encoding='utf-8')  #Открываем файл для записи

    text = ''                                 #Текст, который получится

    # Считываем литеры до первой точки
    while True:
        char = infile.read(1)                 #Считываем по одному символу
        if char == '.':
            break                             #Выходим из цикла, если встретили точку
        if char:                              #Если символ не пустой
            text += char


    for i in range(0, len(text), 40):
        outfile.write(text[i:i + 40] + '\n')  #Записываем по 40 литер и добавляем переход строки


    infile.close()
    outfile.close()


#Создание входного файла
input_file = open('lab6/name/input.txt', 'w', encoding='utf-8')
input_file.write("Какой-то текст для проверки программы, бла бла бла, много текста, хватит. А вот предложение после точки, которое должно исчезнуть.")
input_file.close()







