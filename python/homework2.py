# Создать 2 переменных типа String с разными значениями

name = "Liliya"
surname = "Cherry"

#Создать 4 переменных типа Integer с разными значениями

a = 3
b = 5
c = 10
d = 8
#
# # Создать 3 переменных типа Float с разными значениями
#
f_1 = 2.5
f_2 = 1.5
#
# # Реализовать 15 варианта сравнения int переменных
# # с операторами >, <, >=, <=, !=.
# # результаты весвести в консоль.
#
Life_is_good = True
Life_is_not_good = False

if Life_is_good:
    print("Enjoy you life")
if a == 3:
    print("true")
    if a >= 3:
        print("true")
if a == b:
    print("false")
else:
    print("Life_is_not_good")
if a != b:
    print("true")
if a < c:
    print("Life_is_good")
    if a <= c:
        print("Life_is_good")
    elif a != c:
        print("Life_is_good")
if a+b == d:
    print("Life_is_good")
    if a+b >= d:
        print("Life_is_good")
        if a+b < d:
            print("false")
        else:
            print("Life_is_not_good")
if c > d:
    print("Enjoy you life")
    if c >= d:
        print("Enjoy you life")
        if c == d:
            print("Enjoy you life")
        else:
            print("Life_is_not_good")
print("-----------------------")
#
# # Реализовать 9 варианта сравнения Float переменных
# # с операторами >, <, >=, <=, !=.
# # результаты весвести в консоль.
#
b_true = True
b_false = False

print(f_1 == f_2)
print(f_1 != f_2)
print(f_1 <= f_2)
print(f_1 >= f_2)
print(f_1 > f_2)
print(f_1 < f_2)
print(f_2 != f_1)
print(f_2 >= f_1)
print(f_2 <= f_1)
print("-----------------------")
#
# # Реализовать 10 варианта сравнения int переменных
# # с операторами >, <, >=, <=, !=
# # и условными выражениями (end, or, not).
# # результаты   вывести в консоль.
#
age = 45
weigh = 48
blond = True
salary = 600

result = age < 50 and salary == 600
print(result)
result = age >= 50 and salary <= 600
print(result)
result = age < 50 or salary >= 600
print(result)
result = age <= 50 or weigh == 48
print(result)
result = age == 50 or weigh != 48
print(result)
result = not age <= 50 or weigh == 48
print(result)
result = not age == 50 or weigh == 48
print(result)
result = not age == 50 and weigh == 48
print(result)
result = not age <= 49 or weigh > 48
print(result)
result = not age > 47 or weigh < 48
print(result)
print("---------------------------")
#
# # Сделать скрипт используя функцию input().
# # 1. Функция должна на вход принимать целое число.
# # 2. Выводить должна "Вы вели число = (введённое число)
# # которое (меньше/больше/равно) 30"
#
user_data = int(input("Введите число :  "))

if user_data == 30:
    print("Вы ввели число = 30!  ")

if user_data > 30:
    print("Вы ввели число =", user_data, "которое больше 30! ")

if user_data < 30:
    print("Вы ввели число =", user_data, "которое меньше 30! ")
print("-----------------------------")

# Сделать скрипт используя функцию input().

# 1. Функция должна на вход принимать целое число.

# 2. Внутри функции должно сгенерироваться рандомное целое число
# (import random)...(random.randint(1, 100))

# 3.Выводить должна "Вы вели число = (введённое число)
# которое (меньше/больше/равно) сгенерированному числу"
import random
random_value = random.randint(1, 100)
attempt = 0
print(random_value)

for i in range(1,11):
    user_data = int(input("Введите число :  "))
    if user_data < random_value:
        print("Вы ввели число, меньше рандомного!")
    elif user_data > random_value:
        print("Вы ввели число, больше рандомного! ")
    else:
        print(f"Вы угадали число {random_value} ")

        break













