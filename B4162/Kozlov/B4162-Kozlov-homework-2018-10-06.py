class Figure:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    #def square(self):
        #return self.x * self.y


class Rectangle(Figure):
    def __s(self):
        return self.x * self.y

    def square(self):
        return self.__s()


class Triangle(Figure):
    def __s(self):
        return 0.5 * self.x * self.y

    def square(self):
        return self.__s()

class Parallelepiped(Figure):
    def __s(self):
        return 2 * (self.x * self.y + self.y * self.z + self.x * self.z)
    
    def square(self):
        return self.__s()

rect = Rectangle(1, 2)
print(rect.square())

trgl = Triangle(23, 3)
print(trgl.square())

prlpd = Parallelepiped(1,2,3) #Добавил ещё один параметр для более универсального нахождения площади фигуры, 
                              #в частности 3Д фигуры (параллелепипед). Парадигмы ООП (инкапсуляции, полиморфизма и наследования)
                              #по заданию использованы.
print(prlpd.square())





















































































































