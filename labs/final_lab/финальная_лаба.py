import random

player_alive = True
experience = 0
level_point = 0
current_level = 0
levels = {1: 10, 2: 23, 3: 49, 4: 108, 5: 226, 6: 470, 7: 1000, 8: 2101, 9: 4333}

def choice_error(text, min_value, max_value):
    while True:
        try:
            choice = int(input(text))
        except ValueError:
            print("Введите число!")
            continue

        if choice < min_value or choice > max_value:
            print(f"Выберите один из вариантов!")
            continue

        return choice

base_stats = {
    "Max_HP": random.randint(80, 100),
    "Attack": random.randint(5, 13),
    "Defense": random.randint(0, 5),
    "Agility": random.randint(8, 18),
    "Intellect": random.randint(1, 10),
    "Speed": random.randint(1, 5)
}

Height = 0
Weight = 0

rase = choice_error('какую рассу вы выберите?\n(1) Человек\n'
                    '(2) Эльф\n(3) Дварф\n\033[36m>> \033[0m', 1, 3)

if rase == 1:
    print('Вы выбрали Человескую рассу\n'
          'эта расса универсальна и адаптивна\n'
          'ваши статы имеют средние показатели')
    Height = random.randint(150, 190)
    Weight = random.randint(50, 100)
    k = (Height + Weight) / 1000
    base_stats["Max_HP"] += 10 + round(10*k)
    base_stats["Attack"] += 6 + round(7*k)
    base_stats['Defense'] += 4
    base_stats['Agility'] += 4
    base_stats['Intellect'] += 5
    base_stats['Speed'] += 2

elif rase == 2:
    print('Вы выбрали Эльфийскую рассу\n'
              'эта расса утончённая и магически одарённая\n'
              'ваши статы смещены в сторону ловкости')
    Height = random.randint(170, 210)
    Weight = random.randint(50, 90)
    k = (Height + Weight) / 1000
    base_stats['Max_HP'] += 1 + round(1*k)
    base_stats['Attack'] += 4 + round(5*k)
    base_stats['Defense'] += 5
    base_stats['Agility'] += 9
    base_stats['Intellect'] += 9
    base_stats['Speed'] += 4

elif rase == 3:
    print('Вы выбрали Дварфскую рассу\n'
              'эта расса крепкая и выносливая\n'
              'ваши статы смещены в сторону силы')
    Height = random.randint(110, 160)
    Weight = random.randint(40, 90)
    k = (Height + Weight)/1000
    base_stats['Max_HP'] += 15 + round(15*k)
    base_stats['Attack'] += 10 + round(12*k)
    base_stats['Defense'] += 8
    base_stats['Agility'] += 0
    base_stats['Intellect'] += 1
    base_stats['Speed'] += 1

stats = base_stats.copy()
stats['HP'] = stats["Max_HP"]

def print_stats():
    for key, value in levels.items():
        if current_level == key - 1:
            up_lvl = value
    print(f"Опыт: {experience} из {up_lvl}\nУровень персонажа: {current_level}\n"
          f"Жизни: {stats['HP']} из {stats['Max_HP']}\nАтака: {stats['Attack']}\n"
          f"Защита: {stats['Defense']}\nЛовкость: {stats['Agility']}\n"
          f"Интеллект: {stats['Intellect']}\nСкорость: {stats['Speed']}\n"
          f"Рост: {Height}\nВес: {Weight}")
print_stats()

weapons_l1 = {
    "Ржавый меч": {"type": "weapon", "Attack": 3},
    "Камень": {"type": "weapon", "Attack": 4},
    "Крестьянские вилы": {"type": "weapon", "Attack": 6},
    "Деревяный лук": {"type": "weapon", "Attack": 4, "scaling": {"Agility": 0.3}},
    "Магический посох": {"type": "weapon", "Attack": 3, "scaling": {"Intellect": 0.5}},
    "Охотничий нож": {"type": "weapon", "Attack": 5},
    "Кинжал": {"type": "weapon", "Attack": 6},
    "Гоблинское копьё": {"type": "weapon", "Attack": 5, "scaling": {"Intellect": 0.6}}
}

weapons_l2 = {
    "Ржавый меч": {"type": "weapon", "Attack": 3},
    "Камень": {"type": "weapon", "Attack": 4},
    "Крестьянские вилы": {"type": "weapon", "Attack": 6},
    "Деревяный лук": {"type": "weapon", "Attack": 4, "scaling": {"Agility": 0.3}},
    "Магический посох": {"type": "weapon", "Attack": 3, "scaling": {"Intellect": 0.5}},
    "Магический посох с рубином": {"type": "weapon", "Attack": 4, "scaling": {"Intellect": 0.6}},
    "Охотничий нож": {"type": "weapon", "Attack": 5},
    "Кинжал": {"type": "weapon", "Attack": 6},
    "Стальной меч": {"type": "weapon", "Attack": 10},
    "Двуручный меч": {"type": "weapon", "Attack": 15},
    "Сабля": {"type": "weapon", "Attack": 9, "scaling": {"Agility": 0.2}},
    "Рапира": {"type": "weapon", "Attack": 7, "scaling": {"Agility": 0.3}},
    "Гоблинское копьё": {"type": "weapon", "Attack": 5, "scaling": {"Intellect": 0.6}},
    "Топор": {"type": "weapon", "Attack": 13}
}

weapons_l3 = {
    "Ржавый меч": {"type": "weapon", "Attack": 3},
    "Камень": {"type": "weapon", "Attack": 4},
    "Крестьянские вилы": {"type": "weapon", "Attack": 6},
    "Деревяный лук": {"type": "weapon", "Attack": 4, "scaling": {"Agility": 0.3}},
    "Эльфийский лук": {"type": "weapon", "Attack": 6, "scaling": {"Agility": 0.4, "Intellect": 0.4}},
    "Изысканный лук": {"type": "weapon", "Attack": 8, "scaling": {"Agility": 0.5} },
    "Магический посох": {"type": "weapon", "Attack": 3, "scaling": {"Intellect": 0.5}},
    "Магический посох с рубином": {"type": "weapon", "Attack": 4, "scaling": {"Intellect": 0.6}},
    "Магический шар": {"type": "weapon", "Attack": 10, "scaling": {"Intellect": 0.5}},
    "Магический меч": {"type": "weapon", "Attack": 15, "scaling": {"Intellect": 0.6}},
    "Охотничий нож": {"type": "weapon", "Attack": 5},
    "Кинжал": {"type": "weapon", "Attack": 6},
    "Стальной меч": {"type": "weapon", "Attack": 10},
    "Двуручный меч": {"type": "weapon", "Attack": 15},
    "Королевский меч": {"type": "weapon", "Attack": 16, "scaling": {"Defense": 0.6}},
    "Сабля": {"type": "weapon", "Attack": 9, "scaling": {"Agility": 0.2}},
    "Рапира": {"type": "weapon", "Attack": 7, "scaling": {"Agility": 0.3}},
    "Гоблинское копьё": {"type": "weapon", "Attack": 5, "scaling": {"Intellect": 0.6}},
    "Топор": {"type": "weapon", "Attack": 13},
    "Двусторонний топор": {"type": "weapon", "Attack": 17},
    "Гномья булава": {"type": "weapon", "Attack": 20}
}

armors_l1_2 = {
    "Кожаная броня": {"type": "armor", "Defense": 1},
    "Мантия": {"type": "armor", "Defense": 1},
    "Латы": {"type": "armor", "Defense": 2, "Speed": -0.5},
    "Охотничья накидка": {"type": "armor", "Defense": 2},
    "Доспех наёмника": {"type": "armor", "Defense": 3, "Speed": -1},
    "Рыцарские доспехи": {"type": "armor", "Defense": 4, "Speed": -2, "Agility": -2},
    "Броня пехотинца": {"type": "armor", "Defense": 4, "Speed": -3},
    "Бойцовские обноски": {"type": "armor", "Defense": 3},
}

armors_l3 = {
    "Кожаная броня": {"type": "armor", "Defense": 1},
    "Мантия": {"type": "armor", "Defense": 1},
    "Латы": {"type": "armor", "Defense": 2, "Speed": -0.5},
    "Винная бочка": {"type": "armor", "Defense": 9, "Speed": -99, "Agility": -99},
    "Охотничья накидка": {"type": "armor", "Defense": 2},
    "Доспех наёмника": {"type": "armor", "Defense": 3, "Speed": -1},
    "Рыцарские доспехи": {"type": "armor", "Defense": 4, "Speed": -2, "Agility": -2},
    "Броня пехотинца": {"type": "armor", "Defense": 4, "Speed": -3},
    "Тяжелая броня": {"type": "armor", "Defense": 5, "Speed": -4, "Agility": -4},
    "Бойцовские обноски": {"type": "armor", "Defense": 3},
    "Броня с шипами": {"type": "armor", "Defense": 5, "Speed": -2, "Agility": -8, "Attack": 5},
    "Королевская броня": {"type": "armor", "Defense": 5},
    "Подозрительная тёмная ткань": {"type": "armor", "Defense": 2, "Speed": 1, "Agility": 4, "Intellect": 6}
}

dungeon_items = {
    "Малое зелье лечения": {"type": "potion", "HP": 6},
    "Среднее зелье лечения": {"type": "potion", "HP": 14},
    "Большое зелье лечения": {"type": "potion", "HP": 32},
    "Зелье берсерка": {"type": "potion", "Defense": -2, "Speed": 1, "Attack": 7},
    "Склянка с чёрной смолой": {"type": "potion", "Max_HP": -10, "Intellect": 8},
    "Блёвбургер": {"type": "potion", "Max_HP": -80, "Defense": 10},
    "Амулет удачи": {"type": "passive", "Speed": 2, "Agility": 4},
    "Амулет скорости": {"type": "passive", "Speed": 4},
    "Амулет силы": {"type": "passive", "Attack": 8},
    "Филосовский камень": {"type": "passive", "Defense": 4, "Intellect": 4},
    "Сборник работ великих филосовов": {"type": "passive", "Intellect": 15},
    "Гномий щит": {"type": "passive", "Defense": 2},
    "Гномьи сапоги": {"type": "passive", "Speed": 2},
    "Тяжелые наручи": {"type": "passive", "Attack": 2, "Defense": 2, "Speed": -1},
    "Зачарованный медальон": {"type": "passive", "Defense": 1, "Attack": 2, "Agility": 2},
    "Четырехлистный клевер": {"type": "passive", "Agility": 6},
    "Рунный камень Сварог": {"type": "passive", "Defense": 3, "Attack": 6},
    "Рунный камень Велес": {"type": "passive", "Defense": 2, "Agility": 3, "Intellect": 5},
    "Лунный браслет": {"type": "passive", "Speed": 1, "Agility": 4},
    "Ритуальная маска": {"type": "passive", "Defense": 2, "Attack": 10, "Speed": -4, "Intellect": -8},
    "Пояс наёмного убийцы": {"type": "passive", "Max_HP": 15, "Attack": 4},
    "Пояс бандита": {"type": "passive", "Max_HP": 10, "Attack": 1},
    "Пояс силача": {"type": "passive", "Max_HP": 20, "Attack": 6},
    "Драконий коготь": {"type": "passive", "Defense": 2, "Attack": 3, "Speed": 1, "Intellect": 2,
                        "Agility": 3, "Max_HP": 8},
    "Ловец снов": {"type": "passive", "Speed": 1, "Agility": 3, "Intellect": 4},
    "Реликт в камне": {"type": "passive", "Max_HP": 3, "Attack": 2}
}

enemy_items = {
    "Потраха": {"type": "potion", "HP": 3},
    "Кишки": {"type": "potion", "HP": 2},
    "Объедки": {"type": "potion", "HP": 4},
    "Мясо": {"type": "potion", "HP": 6},
    "Малое зелье лечения": {"type": "potion", "HP": 10},
    "Среднее зелье лечения": {"type": "potion", "HP": 25},
    "Большое зелье лечения": {"type": "potion", "HP": 60}
}

enemies_l1 = {
    "Гоблин": {"HP": 25, "Attack": 10, "Speed": 8, "experience": 5, "Defense": 7},
    "Скелет": {"HP": 30, "Attack": 15, "Speed": 6, "experience": 5, "Defense": 2},
    "Гончая": {"HP": 15, "Attack": 25, "Speed": 9, "experience": 8, "Defense": 0},
    "Орк": {"HP": 40, "Attack": 20, "Speed": 6, "experience": 12, "Defense": 10},
}

enemies_l2 = {
    "Гончая": {"HP": 15, "Attack": 25, "Speed": 9, "experience": 8, "Defense": 0},
    "Орк": {"HP": 40, "Attack": 20, "Speed": 6, "experience": 12, "Defense": 10},
    "Тролль": {"HP": 55, "Attack": 30, "Speed": 4, "experience": 19, "Defense": 6},
    "Тёмный маг": {"HP": 40, "Attack": 33, "Speed": 15, "experience": 26, "Defense": 14},
}

enemies_l3 = {
    "Адская Гончая": {"HP": 30, "Attack": 40, "Speed": 12, "experience": 26, "Defense": 3},
    "Тёмный маг": {"HP": 40, "Attack": 33, "Speed": 99, "experience": 26, "Defense": 14},
    "Армия Орков": {"HP": 100, "Attack": 35, "Speed": 7, "experience": 50, "Defense": 20},
    "Тролль": {"HP": 55, "Attack": 30, "Speed": 4, "experience": 19, "Defense": 6},
    "Банда гоблинов": {"HP": 80, "Attack": 30, "Speed": 10, "experience": 32, "Defense": 15},
    "Орда скелетов": {"HP": 80, "Attack": 45, "Speed": 7, "experience": 40, "Defense": 8},
    "Дракон": {"HP": 70, "Attack": 60, "Speed": 6, "experience": 60, "Defense": 20},
}

enemies_l4 = {
    "Тёмный маг": {"HP": 40, "Attack": 33, "Speed": 99, "experience": 26, "Defense": 14},
    "Армия Орков": {"HP": 100, "Attack": 35, "Speed": 7, "experience": 50, "Defense": 20},
    "Орда скелетов": {"HP": 80, "Attack": 45, "Speed": 7, "experience": 40, "Defense": 8},
    "Дракон": {"HP": 70, "Attack": 60, "Speed": 6, "experience": 60, "Defense": 20},
    "Инсектоид-солдат": {"HP": 50, "Attack": 70, "Speed": 11, "experience": 91, "Defense": 33},
    "Лич": {"HP": 40, "Attack": 85, "Speed": 14, "experience": 130, "Defense": 40}
}

inventory = []
inventory_limit = 10

equipment = {
    "weapon": None,
    "armor": None
}

def recalculation_stats():
    global stats
    current_hp = stats.get("HP")
    stats = base_stats.copy()

    for slot, item in equipment.items():
        if item:
            for stat, value in item.items():
                if stat != "type" and stat != "name" and stat != "scaling":
                    stats[stat] += value

    for item in inventory:
        if item.get("type") == "passive":
            for stat, value in item.items():
                if stat != "type" and stat != "name":
                    stats[stat] += value

    stats["HP"] = min(current_hp, stats["Max_HP"])

def add_to_inventory(item_name):

    if item_name in dungeon_items:
        item_data = dungeon_items[item_name].copy()
    elif item_name in weapons_l1:
        item_data = weapons_l1[item_name].copy()
    elif item_name in weapons_l2:
        item_data = weapons_l2[item_name].copy()
    elif item_name in weapons_l3:
        item_data = weapons_l3[item_name].copy()
    elif item_name in armors_l1_2:
        item_data = armors_l1_2[item_name].copy()
    elif item_name in armors_l3:
        item_data = armors_l3[item_name].copy()
    elif item_name in enemy_items:
        item_data = enemy_items[item_name].copy()

    item_data["name"] = item_name

    if len(inventory) >= inventory_limit:
        print("Инвентарь полон!\n"
              "Вы можете выбросить предмет из инвентаря, чтобы получить новый")
        for i, item in enumerate(inventory):
            print(f"({i + 1}) {item['name']} ({item['type']})")
        print(f"({i + 2}) Отмена")
        choice = choice_error('\033[36m>> \033[0m', 1, i+2)
        if choice == i + 2:
            print("Вы не стали брать предмет и продолжили путь")
            return
        item = inventory[choice - 1]
        print(f"Предмет \033[4m{item['name']}\033[0m был уничтожен")
        inventory.remove(item)

    inventory.append(item_data)
    print(f"\033[4m{item_name}\033[0m добавлен в инвентарь")

def print_equipment():
    print("Экипировка:")

    if equipment["weapon"]:
        print(f"Оружие: {equipment['weapon']['name']}")
    else:
        print("Оружие: [пусто]")

    if equipment["armor"]:
        print(f"Броня: {equipment['armor']['name']}")
    else:
        print("Броня: [пусто]")

    print()

def open_inventory():
    global stats, inventory

    while True:
        if not inventory:
            print("Инвентарь пуст")
            break

        print_equipment()
        print("Ваш инвентарь:")
        for i, item in enumerate(inventory):
            print(f"({i+1}) {item['name']} ({item['type']})")
        print(f"({i+2}) Назад")

        choice = choice_error("\033[36m>> \033[0m", 1, i+2)
        if choice == i+2:
            break

        item = inventory[choice - 1]
        if item["type"] == "passive":
            while True:
                print(f"{item['name']} ({item['type']})")
                for stat, value in item.items():
                    if stat != "type" and stat != "name":
                        if value > 0:
                            print(f"\033[32m{stat}: +{value}\033[0m")
                        else:
                            print(f"\033[31m{stat}: {value}\033[0m")
                print(f'(1) Выбросить предмет\n(2) Назад')
                choice = choice_error("\033[36m>> \033[0m", 1, 2)
                if choice == 2:
                    break
                elif choice == 1:
                    inventory.remove(item)
                    recalculation_stats()
                    print("Предмет уничтожен")
                    break

        elif item["type"] == "potion":
            while True:
                print(f"{item['name']} ({item['type']})")
                for stat, value in item.items():
                    if stat != "type" and stat != "name":
                        if stat == "HP":
                            print(f"\033[32mВосстанавливает {item['HP']} здоровья\033[0m")
                        else:
                            if value > 0:
                                print(f"\033[32m{stat}: +{value}\033[0m")
                            else:
                                print(f"\033[31m{stat}: {value}\033[0m")
                print(f'(1) Использовать\n(2) Выбросить предмет\n(3) Назад')
                choice = choice_error("\033[36m>> \033[0m", 1, 3)
                if choice == 3:
                    break
                elif choice == 2:
                    inventory.remove(item)
                    print("Предмет уничтожен")
                    break
                elif choice == 1:
                    if "HP" in item:
                        stats["HP"] = min(stats["HP"] + item['HP'], stats["Max_HP"])
                    else:
                        for stat, value in item.items():
                            if stat != "type" and stat != "name":
                                base_stats[stat] += value
                        recalculation_stats()
                    inventory.remove(item)
                    print("Зелье использовано")
                    break

        elif item["type"] == "weapon" or item["type"] == "armor":
            if item["type"] == "weapon":
                slot = 'weapon'
            else:
                slot = 'armor'
            while True:
                print(f"{item['name']} ({item['type']})")
                for stat, value in item.items():
                    if stat != "type" and stat != "name" and stat != "scaling":
                        if value > 0:
                            print(f"\033[32m{stat}: +{value}\033[0m")
                        else:
                            print(f"\033[31m{stat}: {value}\033[0m")
                    if stat == 'scaling':
                        for st, cef in item['scaling'].items():
                            print(f'Усиление урона на \033[32m{cef}\033[0m от \033[32m{st}\033[0m')

                print(f'(1) Экипировать\n(2) Выбросить предмет\n(3) Назад')
                choice = choice_error("\033[36m>> \033[0m", 1, 3)
                if choice == 3:
                    break
                elif choice == 2:
                    inventory.remove(item)
                    print('Предмет уничтожен')
                    break
                elif choice == 1:
                    if equipment[slot]:
                        inventory.append(equipment[slot])
                        print(f"Предмет \033[4m{equipment[slot]['name']}\033[0m снят")

                    equipment[slot] = item
                    inventory.remove(item)
                    recalculation_stats()
                    print(f"Предмет \033[4m{item['name']}\033[0m экипирован")
                    break

def chill_room():
    global level_point
    print('Зайдя в комнату вы чувствуете умиротворение\n'
          'Здесь можно отдохнуть и восстановить силы')
    while True:
        print('(1) Посмотреть статы\n'
              '(2) Открыть инвентарь\n'
              '(3) Продолжить путь')
        chill_room = choice_error('\033[36m>> \033[0m', 1, 3)
        if chill_room == 1:
            while True:
                print('Ваши статы:')
                print_stats()
                print('(1) Распределить очки уровня\n'
                      '(2) Назад')
                choice = choice_error('\033[36m>> \033[0m', 1, 2)
                if choice == 1:
                    while level_point >= 1:
                        print(f'Доступные очки: {level_point}')
                        lvl_up = choice_error('(1) +2 к атаке\n(2) +5 к максимальному здоровью\n'
                                              '(3) +2 к защите\n(4) +0.5 к скорости\n(5) +3 к ловкости\n'
                                              '\033[36m>> \033[0m', 1, 5)
                        if lvl_up == 1:
                            base_stats['Attack'] += 2
                        elif lvl_up == 2:
                            base_stats['Max_HP'] += 5
                        elif lvl_up == 3:
                            base_stats['Defense'] += 2
                        elif lvl_up == 4:
                            base_stats['Speed'] += 0.5
                        elif lvl_up == 5:
                            base_stats['Agility'] += 5
                        level_point -= 1
                        recalculation_stats()
                    print('Сейчас у вас нет доступных очков')
                else:
                    break

        elif chill_room == 2:
            open_inventory()
        else:
            print('Отходя от уютного костра, вы продолжаете путь')
            break

def random_enemy(lvl_room_now):
    if lvl_room_now == 1:
        name, data = random.choice(list(enemies_l1.items()))
    elif lvl_room_now == 2:
        name, data = random.choice(list(enemies_l2.items()))
    elif lvl_room_now == 3:
        name, data = random.choice(list(enemies_l3.items()))
    elif lvl_room_now == 4:
        name, data = random.choice(list(enemies_l4.items()))
    enemy = data.copy()
    enemy['name'] = name
    return enemy

def random_drop_enemy_item():
    enemy_drop, stat = random.choice(list(enemy_items.items()))
    return enemy_drop

def calculate_enemy_damage(atk_enemy):
    damage = atk_enemy - stats['Defense']

    dodge_chance = 10 + stats['Agility']
    if random.randint(1, 100) <= dodge_chance:
        print('Вам удалось \033[32mуввернуться\033[0m от атаки')
        return 0

    return max(damage, 1)

def calculate_player_damage(enemy_def):
    damage = stats['Attack']
    if equipment['weapon'] and 'scaling' in equipment['weapon']:
        for stat, cef in equipment['weapon']['scaling'].items():
            damage += stats[stat] * cef

    crit_chance = 5 + (stats['Intellect']/2)
    if random.randint(1, 100) <= crit_chance:
        print('Вы нанесли \033[31mкритический\033[0m удар')
        damage *= 1.5

    return max(damage - enemy_def, 1)

def battle_room():
    global experience, level_point, current_level, player_alive, lvl_room_now
    enemy = random_enemy(lvl_room_now)

    enemy_texts = {
        "Гоблин": "Заходя в комнату вы слышите звонкий смех",
        "Скелет": "Вы заходите в комнату\nГлухой стук костей вызывает у вас мурашки",
        "Гончая": "Едва ваша нога успела ступить в комнату",
        "Орк": "По пощере разносится злобное фырканье",
        "Тролль": "В нос ударила ужасная вонь",
        "Тёмный маг": "Жуткий холодок прошёл по коже",
        "Адская гончая": "Комната пропитана жаром",
        "Банда гоблинов": "Звон монет и гулкий смех раздаются вокруг",
        "Орда скелетов": "Вы слышите как груда костей подбирается из тени",
        "Армия орков": "В воздухе чувствуется вкус крови",
        "Дракон": "Вы видите своё отражение в гигантском жёлтом глазу",
        "Инсектоид-солдат": "Противное жужжание окутало комнату",
        "Лич": "Перед вами сама смерть"
}
    
    print(enemy_texts.get(enemy['name']))
    print(f"На вас нападает \033[31m{enemy['name']}\033[0m")

    input('\033[36mEnter >> \033[0m')

    player_turn = stats['Speed'] >= enemy['Speed']
    if player_turn:
        print('Вы оказались быстрее\n'
              'Первый удар за \033[32mвами\033[0m')
    else:
        print(f'Противник оказался быстрее\n'
              f"\033[31m{enemy['name']}\033[0m делает первый удар")

    while stats['HP'] > 0 and enemy['HP'] > 0:
        if player_turn:
            print(f'Ваше Здоровье: {stats["HP"]}/{stats["Max_HP"]}\n'
                  f'Здоровье Врага: {enemy["HP"]}\n'
                  f'(1) Атаковать\n(2) Открыть инвентарь')

            choice = choice_error('\033[36m>> \033[0m', 1, 2)
            if choice == 1:
                atk = calculate_player_damage(enemy['Defense'])
                enemy['HP'] -= atk
                print(f'Вы нанесли {atk} урона')
            elif choice == 2:
                open_inventory()

        if enemy['HP'] <= 0:
            print('Враг повержен')
            experience += enemy['experience']
            add_to_inventory(random_drop_enemy_item())
            print(f'Получено опыта: \033[32m{enemy["experience"]}\033[0m')

            for lvl, exp in levels.items():
                if experience >= exp and current_level < lvl:
                    current_level = lvl
                    level_point += 1
                    print(f'Уровень персонажа \033[32mповышен\033[0m\n'
                          f'Текущий уровень: \033[32m{current_level}\033[0m\n'
                          f'Очки уровня: \033[32m+1\033[0m')

        if enemy['HP'] <= 0:
            input('\033[36mEnter >> \033[0m')
            break
        input('\033[36mEnter >> \033[0m')
        print(f"{enemy['name']} атакует")
        atk = calculate_enemy_damage(enemy['Attack'])
        stats['HP'] -= atk
        print(f'Вы получили {atk} урона')
        player_turn = True

        if stats['HP'] <= 0:
            player_alive = False
            print('\033[31mСмерть\033[0m настигла вас')
            break

def random_item(lvl_room_now):
    if lvl_room_now == 1:
        weapons = list(weapons_l1.keys())
        armors = list(armors_l1_2.keys())
    elif lvl_room_now == 2:
        weapons = list(weapons_l2.keys())
        armors = list(armors_l1_2.keys())
    elif lvl_room_now == 3:
        weapons = list(weapons_l3.keys())
        armors = list(armors_l3.keys())
    pool = list(dungeon_items.keys()) + weapons + armors
    return random.choice(pool)

def chest_room():
    global lvl_room_now
    print('Вы заходите в небольшую обветшалую комнату\n'
          'перед вами старинный сундук укутанный паутиной\n'
          'Хотите ли вы его открыть?\n'
          '(1) Открыть\n'
          '(2) Пройти мимо')
    choice = choice_error('\033[36m>> \033[0m', 1, 2)
    if choice == 2:
        return
    elif choice == 1:
        print('Вы с осторожностью подходите ближе\n'
              'Смахивая пыль вы открываете сундук')
        item_name = random_item(lvl_room_now)
        print(f'Вы получили \033[4m{item_name}\033[0m')
        add_to_inventory(item_name)
        recalculation_stats()
        input('\033[36mПродолжить путь Enter >> \033[0m')
        return

def random_room():
    rooms = ['враг', 'сундук', 'отдых']
    room = random.choice(rooms)
    visible = [True, False]
    visible_room = random.choice(visible)
    return room, visible_room

room = 0
lvl_room_now = 1
lvl_room = {2: 30, 3: 60, 4: 90}

def dungeon():
    global room, lvl_room_now
    print('Вы входите в подземелье\n'
          'Тьма и запах сырости окутывают вас\n'
          'Издалека слышны жуткие звуки\n'
          'Вы решаетесь продвигаться вглубь')
    input('\033[36mEnter >> \033[0m')
    while player_alive == True:

        for lvl, room_cnt in lvl_room.items():
            if room >= room_cnt and lvl_room_now < lvl:
                lvl_room_now = lvl
                print(f"\033[35m_____________________________\033[0m\n"
                      f"Сложность подземелья повышена\n"
                      f"Уровень подземелья \033[35m{lvl_room_now}\n"
                      f"_____________________________\033[0m")

        print('Вы наткнулись на развику...')
        left_room, visible_left_room = random_room()
        right_room, visible_right_room = random_room()

        if visible_left_room == True:
            print(f'(1) Левая комната: {left_room}')
        else:
            print('(1) Левая комната: ???')

        if visible_right_room == True:
            print(f'(2) Правая комната: {right_room}')
        else:
            print('(2) Правая комната: ???')

        choice_room = choice_error('\033[36mКуда пойти? >> \033[0m', 1, 2)
        if choice_room == 1:
            player_room = left_room
        else:
            player_room = right_room

        if player_room == 'отдых':
            room += 1
            chill_room()
        elif player_room == 'сундук':
            room += 1
            chest_room()
        elif player_room == 'враг':
            room += 1
            battle_room()

print('Перед тем как отправиться в поход\n'
      'Вы решили прихватить зелье лечения')
add_to_inventory("Малое зелье лечения")

input("\033[36mНажмите Enter, чтобы продолжить >> \033[0m")
dungeon()