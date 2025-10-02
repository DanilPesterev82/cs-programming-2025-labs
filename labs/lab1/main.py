var1 = 5
var2 = 2.5
var3 = "лаба"
var4 = False
print(var1, var2, var3, var4) #Задание 1

name = "Даниил"
age = 20
print(name, age) #Задание 2

a1 = 342
a2 = 56.2
a3 = "43"
c = a1 + a2 + int(a3)
print(c) #Задание 3

a = 3
b = 8
c2 = (a + 4 * b) * (a - 3 * b) + a**2
print(c2) #Задание 4

l = int(input("Введите l:"))
h = int(input("Введите h:"))
print("Площадь =", l * h)
print("Периметр =", 2* (l + h)) #Задание 5

print("*   *   *")
print(" * * * *")
print("  *   *") #Задание 6

d = 12
f = 18
print(d+f, d-f, d*f, d/f, d//f, d%f, d**f)
print(d==f, d!=f, d>f, d<f, d>=f, d<=f) #Задание 7

name1 = "Даниил"
age1 = 20
print(f"Меня зовут {name1}, мне {age1} лет") #Задание 8

g1 = "Съешь ещё "
g2 = "этих мягких "
g3 = "французских булок, "
g4 = "да выпей "
g5 = "чаю"
print(g1 + g2 + g3 + g4 + g5) #Задание 9

print(4 * "Нет! Да! ") #Задание 10

n = input("Введите 3 числа, разделённых запятой:")
n1, n2, n3 = n.split(",")
result = (int(n1) + int(n3)) // int(n2)
print(f"результат: {result}") #Задание 11

word = (str(input("Введите слово, содержащее не менее 10 символов:")))
print(word[:4])
print(word[-2:])
print(word[3:8])
print(word[::-1]) #Задание 12