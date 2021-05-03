#1. В отеле есть 3 типа номеров: royal (2-3 комнаты), lux (1-2 комнаты), standard (1 комната). надо добавить метод для создания номеров и хранения их в виде словаря.

#2. В комнате есть мебель для ванной, спальни и зала (если есть зал). нужно добавить метод для добавления и удаления из комнаты мебели в любом количестве.

#3. Нужно создать один метод для изменения любого номера по заданным параметрам, в том числе удалению и изменению номеров и комнат.

class Hotel():
    def __init__(self, x, y, z):
        self.royal = x
        self.lux = y
        self.standart = z
rooms = Hotel(3, 2, 1)
print(rooms.__dict__)
print(' ')

#В комнате есть мебель для ванной, спальни и зала (если есть зал). нужно добавить метод для добавления и удаления из комнаты мебели в любом количестве.
class Room():
    def __init__(self, bedroom, bathroom, main_room):
        self.bedroom = bedroom
        self.bathroom = bathroom
        self.main_room = main_room

    def edit(self):
        print("если добавляешь мебель введи просто число, если удаляешь число со знаком - ")
        self.bedroom = self.bedroom + int(input("введите кол-во "))
        if self.bathroom < 0:
            self.bathroom = int(input("Error"))
        self.bathroom = self.bathroom + int(input("введите кол-во "))
        if self.bathroom < 0:
            self.bathroom = int(input("Error"))
        self.main_room = self.main_room + int(input("введите кол-во "))
        if self.main_room < 0:
            self.main_room = int(input("Error"))

room_1 = Room(3, 2, 1)
print(room_1.__dict__)
room_1.edit()
print(room_1.__dict__)

