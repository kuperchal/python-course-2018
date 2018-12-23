class dengi:
     def __init__(self,dengi,sber):
         self.dengi=dengi
         self.sber=sber

     def info(self):
         print('Nal:' + str(self.dengi))
         print('Sber:' + str(self.sber))

class pay(dengi):
     def __init__(self,dengi,sber,k):
         super().__init__(dengi,sber)
         self.k=k

     def plata(self):
        self.dengi=self.dengi - self.k

     def info(self):
         super().info()
         print('Oplata:' + str(self.k))

class food(dengi):
     def __init__(self,dengi,sber,f):
         super().__init__(dengi,sber)
         self.f=f

     def info(self):
         super().info()
         print('Food:' + str(self.f))


tr1=dengi(12000,5000)
gr1=pay(18000,800,3000)
a1=food(17000,2000,1000)
tr1.info()
gr1.plata()
gr1.info()
a1.info()
