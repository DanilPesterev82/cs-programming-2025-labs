name = input("Введите имя: ")
age = input("Ввведите возраст: ")
for i in range(10):
    print(f'Меня зовут {name} и мне {age} лет') #Задание 1

a = input("Введите число от 1 до 9: ")
b = 1
for i in range(10):
    print(a ,'*', b, '=', int(a)*b)
    b += 1 #Задание 2

for i in range(2, 101, 3):
    print(i) #Задание 3

num = int(input("Введите число: "))
var = 1
for i in range(1, num+1):
    var = var * i
print(var) #Задание 4

count = 20
while count >= 0:
    print(count)
    count -= 1 #Задание 5

num1 = int(input("Введите число: "))
i = 0
b = 1
c = 0
print(i)
print(b)
while c < num1:
    c = i + b
    if c > num1:
        break
    else:
        print(c)
        i = b
        b = c #Задание 6

word = input('Введите слово: ')
length_word = len(word)
mas = []
f = 1
for letter in word:
    mas.append(letter)
    mas.append(str(f))
    f += 1
print(*mas, sep='') #Задание 7

while True:
    a, b = input('Введите два числа через пробел: ').split()
    print('Сумма равна = ', int(a) + int(b)) #Задание 8