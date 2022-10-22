from numpy import random
import math 
r_max = 0
width = height = None
def size_matrix():
    global width, height, r_max
    width = int(input('Введите ширину матрицы: '))
    height = width
    r_max = width // 2
    return width, height, r_max
def print_circle_empty():
    print(f'Введите радиус не превышающий {r_max}')
    radius = int(input())
    if radius <= r_max:
        coordinate_y = int(input('Введите значение ординаты центра окружности: '))
        coordinate_x = int(input('Введите значение абсциссы центра окружности: '))
        if width - coordinate_y - radius <= 0 or width - coordinate_x - radius <= 0:
            print('Окружность выходит за пределы матрицы')
        else:
            matrix_zero_empty = [[random.randint(0,1) for j in range(width)] for i in range(height)]
            for y in range(height):
                for x in range(width):
                    if abs((y-coordinate_y)**2 + (x-coordinate_x)**2 - radius**2) <= math.ceil(height/radius):
                        matrix_zero_empty[x][y] = '1'
                    else:
                        matrix_zero_empty[x][y] = '0'
            for rows in matrix_zero_empty:
                print(" ".join(rows))
    else:
        print(f'Радиус превышает максимальное значение {r_max}')
def print_circle():
    if width % 2 == 0:
        x_0 = y_0 = (width-1)/2
        r = width/2
    else:
        x_0 = y_0 = r = width // 2
    n = width/r
    matrix_zero = [[random.randint(0,1) for j in range(width)] for i in range(height)]
    for y in range(height):
        for x in range(width):
            if (y-y_0)**2 + (x-x_0)**2 - r**2 < n:
                matrix_zero[x][y] = '1'
            else:
                matrix_zero[x][y] = '0'
    for row in matrix_zero:
        print(" ".join(row)) # объединяет элементы списка
        
def print_rhomb():
    radius = int(input('Введите значение половины диагонали ромба: '))
    coordinate_x = int(input('Введите значение первой координаты центра ромба: '))
    coordinate_y = int(input('Введите значение второй координаты центра ромба: '))
    matrix_zero_rhomb = [[random.randint(0,1) for j in range(width)] for i in range(height)]
    for y in range(height):
        for x in range(width):
            if (abs(y-coordinate_y))/radius + (abs(x-coordinate_x))/radius == 1:
                matrix_zero_rhomb[x][y] = '1'
            else:
                matrix_zero_rhomb[x][y] = '0'
    for rows in matrix_zero_rhomb:
        print(" ".join(rows))

def main():
    size_matrix()
    way = input('Что желаете нарисовать: круг, окружность или ромб? ')
    if way == 'круг':
        print_circle()
    elif way == 'окружность':
        print_circle_empty()
    elif way == 'ромб':
        print_rhomb()
    else:
        print("Данная опция не существует")

main()
#(y-coordinate_y)**2 + (x-coordinate_x)**2 == radius**2 
#(y-coordinate_y)**2 + (x-coordinate_x)**2 < 2* math.pi * radius: