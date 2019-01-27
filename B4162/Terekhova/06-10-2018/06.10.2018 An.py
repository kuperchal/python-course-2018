class rub:
     def __init__(self,dengi,sber):
         self.dengi=dengi
         self.sber=sber

     def info(self):
         print('Nal:' + str(self.dengi))
         print('Sber:' + str(self.sber))

class dol(rub):
     def __init__(self,dengi,sber,k):
         super().__init__(dengi,sber)
         self.k=k

     def convert(self):
        self.dengi=self.dengi / self.k

     def info(self):
         super().info()
         print('Dollar:' + str(self.dengi))

class euro(rub):
     def __init__(self,dengi,sber,f):
         super().__init__(dengi,sber)
         self.f=f

     def info(self):
         super().info()
         self.dengi=self.dengi / self.f
         print('Euro:' + str(self.dengi))


tr1=rub(12000,5000)
gr1=dol(12000,5000,62)
a1=euro(12000,5000,78)
tr1.info()
gr1.convert()
gr1.info()
a1.info()
