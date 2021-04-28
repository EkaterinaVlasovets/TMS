 #Каждый день в кафе заходит от 5 до 20 покупателей. Каждый покупатель берёт от 1 до 3 чашек кофе.
# Нужно написать функцию, которая будет генерировать тестовые данные при каждом вызове.

import random

def some_day():
    visitors = random.randrange(5, 21)
    coffe_cups = []
    for i in range(1, visitors + 1):
        choise = random.randrange(1, 4)
        coffe_cups.append(choise)
    cups = sum(coffe_cups)
    return visitors, cups

visitors, cups = some_day()

print("Количество кофеманов", visitors)
print("Количество волшебного напитка", cups)


#2. К каждой покупке нужно добавить дату и время до минуты (2 отдельные переменные).
# Время работы кафе - с 9 до 20 часов.
import datetime as dt

def work_time():
   day = dt.date.today()
   day = day.strftime ("%d/%m/%Y")
   print(day)
   list_of_the_time = []
   for cups in range(1, + 1):
       a = random.randrange(9, 20)
       b = random.randrange(0, 59)
       time_1 = dt.time(a, b)
       time_2 = time_1.strftime("%H:%M")
       time_3 = time_2 + "  " + day
       print("Время покупок: ", time_3)
       list_of_the_time.append(time_2)
   return list_of_the_time

list_of_the_time = work_time()

print (work_time)

# 3. Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.

def five_days():
    all_visitors = 0
    all_cups = 0
    for i in range(5):
       all_visitors += some_day()[0]
       all_cups += some_day()[1]

    print( all_visitors, all_cups)




