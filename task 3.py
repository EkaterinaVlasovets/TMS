fruit = ('apple', 'pear', 'cherry', 'banana', 12)
vegetables = ['tomato', 'onion', 'carrot', 17]
berries = ('blueberry', 'cranberry', 'watermelon', 8)
#1. На склад поступил новый товар. Надо пересмотреть склад и исправить ошибки, сделать первую товара букву заглавной.
# Все типы товаров должны быть неизменяемыми, чтобы кто-то случайно не перепутал их снова.


#
#new_berries.append('cherry')


new_fruit = []
for i in fruit[0:-1]:
    new_fruit.append(i.title())


    new_vegetables = []
    for i in vegetables [0:-1]:
        new_vegetables.append(i.title())

new_berries = []
for i in berries [0:-1]:
    new_berries.append(i.title())


#new_fruit.remove('cherry')
#new_berries.append('cherry')



new_fruit = tuple(new_fruit)
new_berries = tuple(new_berries)
new_vegetables = tuple(new_vegetables)

#В овощи забыли добавить капусту. Цифра в категории - это цена товара этого типа.
new_vegetables = list(new_vegetables)
new_vegetables.append('Cabbage')

new_vegetables = tuple(new_vegetables)

print(new_vegetables)
print(new_berries)
print(new_fruit)

#Для удобства хранения, нужно объединить все товары в один объект, при этом сохранить структуру типов.
store = {'Fruit': new_fruit, 'Vegetables': new_vegetables, 'Berries': new_berries}
print(store)

#3. На складе закончились морковка и арбузы. Надо перенести их в категорию "finished".

finished = []
finished.append('Watermelon')
finished.append('Carrot')
print(finished)

#4  Если название продукта длиннее 6 символов, нужно отображать только первые 6.

new_vegetables = list(new_vegetables)
fix_vegetable = []
for x in new_vegetables:
    x = x[0:6]
    fix_vegetable.append(x)
    print(fix_vegetable)

new_berries = list(new_berries)
fix_berries = []
for x in new_berries:
    x = x[0:6]
    fix_berries.append(x)
    print(fix_berries)

new_fruit = list(new_fruit)
fix_fruit = []
for x in new_fruit:
    x = x[0:6]
    fix_fruit.append(x)
    print(fix_fruit)

# 5. На все товары, где есть буква "r", нужно сделать скидку в 20%.
# А если их 2, то 25,5%, и сумму округлить до 2 символов после запятой.
# Рассчитать и вывести на экран стоимость каждого отдельного продукта.


