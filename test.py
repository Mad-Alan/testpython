# Задание 1.
# Создайте словарь, где вместо ключа будет индекс элемента из списка, а вместо
# значения - сам элемент списка.
# Output: dic = {0:92, 1:91, 2:49 ….}
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]
dic = dict(enumerate(lst))
print (dic)


# Задание 2.
# Напишите игру “угадай число”, суть которого заключается в том, что игра с помощью
# модуля random загадывает число от 1 до 20, а пользователь пытается угадать его.
# Если введенное число меньше загаданного, выведите “слишком мало”.Если оно
# больше загаданного, выведите “слишком много
# Если игрок угадал, выведите “Класс! Вы угадали”.”.
# Если попыток было 5 и пользователь не угадал, то выведите “Все, вы не выиграли.
# Игра завершилась”.

print('Игра "Угадай число"')
import random
a = random.randint(1,20)

i = 0

while i < 5:
    b = int(input("Введите число: "))
    if b > a:
        print("слишком много.")
    elif b < a:
        print("слишком мало.")
    elif b == a:
        print("Класс! Вы угадали.")
        break
    i+=1
    if i>=5:
        print("Всё, вы не выиграли. Игра завершилась")

# Задание 3
# Дана строка нечетной длины больше 7 символов, вернуть строку, состоящую из трех
# средних символов данной строки



# Задание 4
# Дается 2 строки ;Aidana; и ;Adilet; . Вам нужно в результате получить смешанную
# строку из двух имен, буква за буквой.
# Output: AAiddialneat

l = "Aidana"
m = "Adilet"
string = l[0] + m[0] + l[1] + m[1] + l[2] + m[2] + l[3] + m[3] + l[4] + m[4] + l[5] + m[5]

print(string)
