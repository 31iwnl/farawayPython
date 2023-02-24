class Info:  # класс для инициализации значения id

    def __init__(self, idx: int):
        self.id = idx

    def get_idx(self):
        return self.id

    def set_idx(self, val):
        self.id = val


class BaseInfo(Info):
    def __init__(self, idx, fio, mail, group):  # инициализация полей
        super().__init__(idx)
        self.fio = fio
        self.mail = mail
        self.group = group

    def __str__(self):  # вывод элементов с перегрузкой
        return f"{self.id} - {self.fio}, {self.mail}, {self.group} "

    def __repr__(self):
        return f"{self.id} - {self.fio}, {self.mail}, {self.group} "

    def __setattr__(self, key, value):
        self.__dict__[key] = value


class File:

    def __init__(self, path):
        self.point = 0
        self.path = path
        self.data = self.Fopen(self.path)

    def __str__(self):  # перегрузка методов __repr__ и  __str__ для вывода данных из файла
        return '\n'.join([str(i) for i in self.data])

    def __repr__(self):
        return f"{[repr(i) for i in self.data]}"

    def __iter__(self):
        return iter(self.data)

    def __next__(self):
        if self.point >= len(self.data):
            self.point = 0
            raise StopIteration
        else:
            self.point += 1
            return self.data[self.point - 1]

    def generator(self):  # генератор коллекции
        self.point = 0
        while self.point < len(self.data):
            yield self.data[self.point]
            self.point += 1

    def sort_id(self) -> list:
        return sorted(self.data, key=lambda f: f.id) #  сортировка по айди

    def sort_fio(self) -> list:
        return sorted(self.data, key=lambda f: f.fio) #  сортировка по фио

    def __getitem__(self, item):  # доступ к элементам коллекции по индексу
        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Такого индекса не существует")

    @staticmethod
    def Fopen(path: str) -> list:  # чтение из файла
        all_data = []

        with open(path, "r") as raw_csv:
            for line in raw_csv:
                (idx, fio, mail, group) = line.replace("\n", "").split(",")
                all_data.append(BaseInfo(int(idx), fio, mail, group))
        return all_data

    def Addstudent(self, idx, fio, mail, group):  # добавление нового студента
        self.data.append(BaseInfo(idx, fio, mail, group))
        self.Fsave(self.path, self.data)

    def find(self) -> list:  # поиск учащихся в группе ИВТАПбд-21
        return [i for i in self.data if i.group == "IVTAPbd-21"]

    @staticmethod
    def Fsave(f, new_data):  # сохранение в файл
        with open(f, "w") as f:
            for element in new_data:
                f.write(f"{element.id},{element.fio},{element.mail},{element.group}\n")


d = File('data-1.csv')


def Mainsub():
    print("Итератор:")
    for i in iter(d):
        print(i)
    print("Генератор:")
    for i in d.generator():
        print(i)
    print("\nДанные (__repr__):\n", repr(d), sep='\n')
    print("Сортировка по именам: ")
    for i in d.sort_fio():
        print(i)
    print("Сортировка по айди: ")
    for i in d.sort_id():
        print(i)
    d.Addstudent(input('Введите айди: '), input('Введите ФИО: '),
                 input('Введите почту: '), input('Введите группу: '))

    print("Учащиеся в группе ИВТАПбд-21: ")
    for i in d.find():
        print(i)
    a = int(input("Введите индекс:"))
    print("Строчка под индексом", a, "->", d.__getitem__(a))


Mainsub()
