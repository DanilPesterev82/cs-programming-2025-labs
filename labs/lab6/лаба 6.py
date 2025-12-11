# Задание 1
time = int(input('введите время: '))
t1 = input('введите исходную единицу измерения: ')
t2 = input('введите, в какую единицу измерения необходимо перевести: ')

def time_transfer(num, original, new):
    if original == 'h':
        hour = num
    elif original == 'm':
        hour = num / 60
    elif original == 's':
        hour = num / 3600

    if new == 'h':
        return hour
    elif new == 'm':
        return hour * 60
    elif new == 's':
        return hour * 3600

print(f'результат: {time_transfer(time, t1, t2)}{t2}')

# Задание 2
deposit = input('Введите сумму вклада и срок хранения через пробел: ')
sum, years = deposit.split(' ')
sum = int(sum)
years = int(years)

def money_back(sum,years):
    p = 0
    money = 0
    p_m = 0
    if sum < 30000:
        return 'Минимальная сумма вклада: 30 000'
    for i in range(1, years + 1):
        ost = sum // 10000
        p = ost * 0.3
        ost = 0
        if p > 5:
            p = 5
        if i <= 3:
            p += 3
        elif i > 3 and i <= 6:
            p += 5
        elif i > 6:
            p += 2
        money += (sum * p)/100
        p_m += money
        sum += money
        money = 0
    return p_m

print(f'результат: {round(money_back(sum, years), 2)}')

# Задание 3
d = input('введите диапазон, числа через пробел: ')
d1, d2 = d.split(' ')
d1 = int(d1)
d2 = int(d2)

def numbers(a, b):
    d = 0
    l = []
    if a > b:
        return 'начало диапазона не может быть больше конца'
    else:
        for i in range(a, b + 1):
            n = i
            for i in range(1, b + 1):
                if n % i == 0:
                    d += 1
            if d == 2:
                l.append(n)
                d = 0
            else:
                d = 0
        return l

print(f'результат: {numbers(d1, d2)}')

# Задание 4
n = int(input('Введите размерность матрицы начиная от 3: '))
if n < 3:
    print("Размерность матрицы должна быть не меньше 3-х")
    exit()

matrix_result = []
matrix1 = []
matrix2 = []

def matrix(m):
    row = []
    for i in range(n):
        row = input(f'Введите строку размерности {n}x{n}: ').split()
        if len(row) != n:
            print('неккоректный ввод')
            exit()
        m.append(list(map(int, row))) #map применяет int к каждому элементу списка
    return m

def matrix_sum(m1, m2, m_r):
    print('матрица 1: ')
    m1 = matrix(m1)
    print('матрица 2: ')
    m2 = matrix(m2)

    for i in range(n):
        row = []
        for j in range(n):
            row.append(m1[i][j] + m2[i][j])
        m_r.append(row)
    return m_r

matrix_result = matrix_sum(matrix1, matrix2, matrix_result)
print('результат: ')
for row in matrix_result:
    print(*row)

# Задание 5
w = input('Введите предложение: ')

def palindrome(word):
    p = []
    for i in word:
        if i.isalpha():
            i = i.lower()
            p.append(i)

    p_new = p[::-1]
    if p == p_new:
        return 'палиндром'
    else:
        return 'не палиндром'

print(f'Это {palindrome(w)}')