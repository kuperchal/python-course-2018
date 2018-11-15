# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:55:02 2018

@author: User
"""
#программа начисления стипендии студентам
#первый класс - студент без стипендии, метод класса выдает только базовая информацию о студенте
class Student:
    def __init__(self, name, year, pay=0):
        self.name = name
        self.year = year
        self.pay = pay
    def showInfo(self):
        bio = (self.name + " year of education is " + str(self.year) + " stipeidia: " + str(self.pay) )
        print (bio)


#подкласс - студент со стипендией, ее метод начисляет стандартную стипендию студенту
class Stipend(Student):
    def __init__(self, name, year, pay=0):
        Student.__init__(self, name, year, pay)
    def stipuha(self):
        self.pay += 1400

#студент-спортсмен, которая зависит от количества мероприятий 
class Sport(Stipend):
    def __init__(self, name, year, events, pay=0):
        Stipend.__init__(self, name, year, pay)
        self.events = events
    def stipuha(self):
        self.pay += 1400 + self.events*100
    def showInfo(self):
        bio = (self.name + " year of education is " + str(self.year) + " events number: " + str(self.events) +  " stipeidia: " + str(self.pay) )
        print (bio)



#---------------------------------------------------------------
student1 = Student('Ivanov Ivan', 3)
student1.showInfo()
student2 = Stipend('Ivanova Ivana', 4)
student2.showInfo()
student2.stipuha()
student2.showInfo()
student3 = Sport('Evgen Prosto', 4, 3)
student3.stipuha()
student3.showInfo()