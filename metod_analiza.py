# -*- coding: utf-8 -*-
dimension = 0
check = True
a=True
x, y = 0, 0
def inputting(): ## задаем размерность матрицы и заполняем единичками  
    global array
    print('Введите количество сравниетельных критериев: ', end='') 
    dimension = int(input())
    array = [[1.0]*dimension for i in range (dimension)]
    return dimension

def outputting(): ## вывод матрицы
    for lists in array:
        print(lists)

def filling(x, y): ##заполняем матрицу значениями
    global array
    print('Введите данные попарного сравнения для ', x+1, ' и ', y+1, ' критериев: ', end='')
    array[x][y] = float(input())
    array[y][x] = round(1/array[x][y], 2) ##округляем до 2х знаков после запятой

def choising(): ## реализовываем возможность прекратить работу программы
    global check
    choise = int(input('Чтобы выполнить заново введите 1, для прекращения работы - любой другой символ: '))
    if choise == '1':
        check = True
    else:
        check = False

if __name__ == '__main__': ## выполнение функций
    while check:
        try:
            size = inputting()
        except BaseException:
            continue

        for i in range(0, size):
            for j in range(i + 1 , size):
                a=True
                while a:  ## проверка на правильность вводимого символа
                    try:
                        filling(i, j)
                    except BaseException: 
                        a = True
                        continue
                    a = False
        outputting()
        choising()
        
        
        