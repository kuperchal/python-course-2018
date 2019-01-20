import random
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):    #Метод демонстрирует принцип наследования
        print(self.name, " walking...")

    def __relax(self):   #Метод демонстрирует принцип инкапсуляции
        print(self.name, "relaxing...")

    def display(self):
        print(' Name:', self. name, '\n', 'Age:', self.age, '\n', 'Gender:', self.gender)

    def get_salary(self):
        print(self.name + ', you have no salary...')


class Employee(Person):
    def __init__(self, name, age, gender, salary, money):   #Метод демонстрирует принцип частичного переопределения
        super().__init__(name, age, gender)
        self.salary = salary
        self.money = money

    def get_salary(self):   #Метод демонстрирует принцип полного переопределения
        self.money += self.salary

    def display(self):  #Метод демонстрирует принцип частичного переопределения
        super().display()
        print(' Salary:', self.salary, '\n', 'Money', self.money)


class Athlete(Person):
    def __init__(self, name, age, gender, type):        #Метод демонстрирует принцип частичного переопределения
        super().__init__(name, age, gender)
        self.type = type

    def competition(self):
        r = random.randint(1, 8)
        print(self.name, 'took', r, 'place!')

    def display(self):      #Метод демонстрирует принцип частичного переопределения
        super().display()
        print('Type', self.type)


class Writer(Person):
    def __init__(self, name, age, gender, works):       #Метод демонстрирует принцип частичного переопределения
        super().__init__(name, age, gender)
        self.works = works

    def display(self):      #Метод демонстрирует принцип частичного переопределения
        super().display()
        print(' Works:')
        for i in range(len(self.works)):
            print(' ', i, ':', self.works[i])

    def addWork(self, someWork):       #Метод, добавляющий элемент в массив работ писателя
        self.works.append(someWork)

    def deleteWork(self, i):        #Метод, удаляющий элемент из массива работ писателя
        if i < len(self.works):
            del(self.works[i])
        else:
            print('operation is impossible')

p = Person('Gena', 20, 'male')
p.display()
print('\n')
p.walk()
print('\n')
p.get_salary()
print('\n')
p._Person__relax()
print('\n')

e = Employee('Lena', 30, 'female', 130, 440)
e.display()
print('\n')
e.walk()
print('\n')
e.get_salary()
e.display()
print('\n')

a = Athlete('Alex', 16, 'male', 'swimmer')
a.display()
print('\n')
a.walk()
print('\n')
a.competition()
print('\n')

w = Writer('Anna', 44, 'female',
           ['In Search of Lost Time by Marcel Proust, 1913',
            'Don Quixote by Miguel de Cervantes, 2005',
            'Moby Dick by Herman Melville, 1851'])
w.display()
w.deleteWork(1)
print('\n')
w.walk()
print('\n')
w.addWork('Hamlet by William Shakespeare, 1601')
w.display()
