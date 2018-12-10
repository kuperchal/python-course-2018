class Figure:
    def get_s(self): 
        pass
    def get_type(self):
        pass
#    def __init__(self, x=0, y=0, z=0):
#        self.x = x
#        self.y = y
#        self.z = z

    #def square(self):
        #return self.x * self.y

class Rectangle(Figure):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
#    def __s(self):
    def get_s(self):
        return self.x * self.y
    def get_type(self):
        return "Прямоугольник"

class Triangle_90(Figure):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def get_s(self):
        return 0.5 * self.x * self.y
    def get_type(self):
        return "Прямоугольный_треугольник"

class Parallelepiped(Figure):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def get_s(self):
        return 2 * (self.x * self.y + self.y * self.z + self.x * self.z)
    def get_type(self):
        return "Параллепипед"
    
rect = Rectangle(1, 2)
print(rect.get_s())
print (rect.get_type())

trgl = Triangle_90(23, 3)
print(trgl.get_s())
print (trgl.get_type())

prlpd = Parallelepiped(1,2,3) #Добавил ещё один параметр для более универсального нахождения площади фигуры, 
print(prlpd.get_s())
print (prlpd.get_type())        #в частности 3Д фигуры (параллелепипед). Парадигмы ООП (инкапсуляции, полиморфизма и наследования)
                                            #по заданию использованы.
