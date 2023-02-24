class Taburetka:
    def __init__(self, price, __secret):
        self.price = price
        self.__secret = __secret

    def Priced(self):
        print(f"Цена табуретки: {self.price}")
        # print(f"Секрет: {self.secret}")


class Stol:
    def __init__(self, price, __secret):
        self.price = price
        self.__secret = __secret

    def Priced(self):
        print(f"Цена стола: {self.price}")
        # print(f"Секрет: {self.secret}")


def firstmethod():
    x = int(input("Введите цену табуретки:\n"))
    y = int(input("Введите цену стула:\n"))
    officeTab = Taburetka(x, "Тайник")
    officeStol = Stol(y, "Тайник")
    print("Полиморфизм классов:")
    for i in (officeTab, officeStol):
        i.Priced()


def secondmethod():
    b = int(input("Введите число для примера\n"))
    print("Полиморфизм:")
    print(b, "+", b, " = ", b + b)
    print(b, "+", b, " = ", str(b) + str(b))


class Mother:
    def __init__(self, mage, age):
        self.mage = mage
        self.age = age


class Daughter(Mother):
    def agediff(self):
        return self.mage - self.age


def rel():
    print("Наследование")
    x = int(input("Введите возраст матери:\n"))
    y = int(input("Введите возраст дочери:\n"))
    t1 = Daughter(x, y)
    print("Разница в возрасте:", t1.agediff())


a = int(input("Полиморфмизм классов; Полиморфизм, как поведение метода; Наследование (0, 1, 2)\n"))
if a == 0:
    firstmethod()
elif a == 1:
    secondmethod()
elif a == 2:
    rel()
else:
    print("Ошибка, нет такого варианта!")
