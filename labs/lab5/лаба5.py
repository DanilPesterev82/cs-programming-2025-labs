# Задание 1
nums = [12, 4, 32, 84, 33, 42, 52, 3, 6, 5]
a = -1
for i in nums:
    a += 1
    if i == 3:
        nums[a] = 30
        print(nums)

# Задание 2
nums1 = [12, 4, 32, 84, 33]
a = -1
for i in nums1:
    a += 1
    nums1[a] = i * i

print(nums1)

# Задание 3
nums2 = [1, 15, 3]
a = 0
b = 0
for i in nums2:
    a += 1
    if i > b:
        b = i

print(b / a)

# Задание 4
data = (3, 'f', 2)

if all(isinstance(x, (int, float)) for x in data):
    sorted_data = tuple(sorted(data))
else:
    sorted_data = data

print(sorted_data)

# Задание 5
d = {"Молоко": 100, "сыр": 350, "колбаса": 300}

min_cost = 0
min_name = None
max_cost = 0
max_name = None

for key, value in d.items():
    if min_cost == 0:
        min_cost = value
        min_name = key
    if value < min_cost:
        min_cost = value
        min_name = key

for key, value in d.items():
    if value > max_cost:
        max_cost = value
        max_name = key

print(f'Продукт с наименьшей ценой: {min_name}')
print(f'Продукт с наибольшей ценой: {max_name}')

# Задание 6
lst = ['молоко', 'колбаса', 'cыр', 1]
lst_dict = {}

for i in lst:
    lst_dict[i] = i

print(lst_dict)

# Задание 7
translate = {'молоко': 'milk', 'сыр': 'cheese', 'торт': 'cake'}

word = input('Введите слово: ')
print(translate.get(word, 'Такого слова нет!'))

# Задание 8
import random
game = [
    ('ножницы', 'бумага'), ('ножницы', 'ящерица'),
    ('бумага', 'камень'), ('бумага', 'спок'),
    ('камень', 'ящерица'), ('камень', 'ножницы'),
    ('ящерица', 'спок'), ('ящерица', 'бумага'),
    ('спок', 'ножницы'), ('спок', 'камень')
]
g1 = input('g1 выбор хода: ')
g2 = random.choice(random.choice(game))
winner = None

for first, second in game:
    if first == g1:
        if second == g2:
            winner = g1
    else:
        if first == g2:
            if second == g1:
                winner = g2

print(f'g2: {g2}')
print(f'победитель {winner}')

# Задание 9
shop = ['молоко', 'сыр', 'колбаса', 'пирог', 'каша', 'яблоки', 'сырники']
shop_dict = {}

for i in shop:
    key = i[0]
    if key not in shop_dict:
        shop_dict[key] = []
    shop_dict[key].append(i)

print(shop_dict)

# Задание 10
students = [("Пётр", [5, 4, 3]), ("Даниил", [3, 4, 4]), ("Александр", [4, 5, 5])]
best = {}
mid = 0
a = 0

for key, value in students:
    for i in value:
      a += 1
      mid += i
    mid /= a
    best[key] = round(mid, 1)
    a = 0
    mid = 0

best_student = max(best, key=best.get)
print(f'{best_student} имеет наивысший средний балл: {best[best_student]}')