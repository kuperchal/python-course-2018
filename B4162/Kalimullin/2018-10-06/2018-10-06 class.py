class Transport:
    def __init__(self,force,size,name):
        self.force=force
        self.size=size
        self.name=name

    def __drive(self):
        print('Use:')

    def info(self):
        print('Force:' + str(self.force))
        print('Size:' + str(self.size))
        print('Name:' + self.name)

class Ground(Transport):
    def __init__(self,force,size,name,wheels):
        super().__init__(force,size,name)
        self.wheels=wheels

    def info(self):
        super().info()
        print('Wheels:' + str(self.wheels))
        print('Type: Ground')

class Air(Transport):
    def __init__(self,force,size,name,wing):
        super().__init__(force,size,name)
        self.wing=wing

    def info(self):
        super().info()
        print('Wing:' + str(self.wing))
        print('Type: Air')

tr1=Transport(12,5,'Transport')
gr1=Ground(15,6,'Bus',6)
a1=Air(17,7,'Plane',2)
tr1._Transport__drive()
gr1._Transport__drive()
tr1.info()
gr1.info()
a1.info()