#Задание 1
t = int(input("Введите температуру: "))
if t >= 20:
  print('Кондиционер выключен')
else:
  print('Кондиционер включён')

#Задание 2
month = int(input("Введите месяц: "))
if month <= 2 or month == 12:
  print('Это зима')
elif 2 < month <= 5:
  print('Это весна')
elif 5 < month <= 8:
  print('Это лето')
elif 8 < month <= 11:
  print('Это осень')

#Задание 3
try:
    age = int(input('Введите возраст собаки (в годах):'))
    age_dog = 0
    if 0 < age <= 2:
        for i in range(age):
            age_dog += 10.5
        print(f"Возраст собаки в человеческих годах: {age_dog}")
    elif 2 < age <= 22:
        for i in range(2):
            age_dog += 10.5
        for i in range(age - 2):
            age_dog += 4
        print(f"Возраст собаки в человеческих годах: {age_dog}")
    elif age < 1:
        print('возраст не может быть меньше 1')
    elif age > 22:
        print('возраст не может быть больше 22')
except ValueError:
    print('Введите число, а не строку!')

#Задание 4
number = input('Введите число: ')
mas = [int(m) for m in number]
if mas[-1] % 2 == 0:
    if sum(mas) % 3 == 0:
        print(f'Число {number} делится на 6')
    else:
        print(f'Число {number} не делится на 6')
else:
    print(f'Число {number} не делится на 6')

#Задание 5
p = False

while not p:
    password = input('Введите пароль: ')
    capital_letter = any(letter.isupper() for letter in password)
    lower_letter = any(letter.islower() for letter in password)
    digit = any(d.isdigit() for d in password)
    a = any(not a.isalnum() for a in password)
    if len(password) < 8:
        print('Пароль должен содержать не менее 8 символов!')
    elif not capital_letter:
        print('Пароль должен содержать заглавные буквы!')
    elif not lower_letter:
        print('Пароль должен содержать строчные буквы!')
    elif not digit:
        print('Пароль должен содержать цифры!')
    elif not a:
        print('Пароль должен содержать специальные символы!')
    else:
        print('Пароль успешно сохранён')
        p = True

#Задание 6:
year = int(input('Введите год:'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} - високосный год')
else:
    print(f'{year} - не високосный год')

#Задание 7:
n = input('Введите 3 числа через пробел: ')
n1, n2, n3 = n.split(' ')
if n1 < n2 and n1 < n3:
    print(f'Наименьшее число: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'Наименьшее число: {n2}')
else:
    print(f'Наименьшее число: {n3}')

#Задание 8:
buy = int(input('Введите сумму покупки: '))
if buy in range(0, 1000):
    print('ваша скидка 0%')
    print(f'к оплате: {buy}')
elif buy in range(1000, 5000):
    b_sell = buy // 5
    buy -= b_sell
    print('ваша скидка 5%')
    print(f'к оплате: {buy}')
elif buy in range(5000, 10001):
    b_sell = buy // 10
    buy -= b_sell
    print('ваша скидка 10%')
    print(f'к оплате: {buy}')
elif buy > 10000:
    b_sell = buy // 15
    buy -= b_sell
    print('ваша скидка 15%')
    print(f'к оплате: {buy}')

#Задание 9
time = int(input('Введите час (0–23): '))
if time in range(0, 6):
    print('сейчас ночь')
elif time in range(6, 12):
    print('сейчас утро')
elif time in range(12, 18):
    print('сейчас день')
elif time in range(18, 24):
    print('сейчас вечер')

#Задание 10
number = input('Введите число: ')
d = 0

if not number.isdigit():
    print('Введите целое число')
else:
    if int(number) <= 1:
        print('Число должно быть больше 1!')
    else:
        for i in range(1, int(number) + 1):
            if int(number) % i == 0:
                d += 1

        if d == 2:
            print(f'{number} - простое число')
        else:
            print(f'{number} - сотавное число')