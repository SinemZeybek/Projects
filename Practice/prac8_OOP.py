from datetime import date
import datetime

     #OBJECT ORIENTED PROGRAMMING
#class: Ortak ozellikleri olan nesneleri gruplandiriyoruz. class`tan uretilmis ornek(instance) 

class workers:
    def __init__(self,name,surname="Unknown",age=0):   #initialize fonk, baslatmak olusturmak icin kullaniyoruz.
        
        self.name = name
        self.surname = surname
        self.age = age                     #self = olusturulan degisken (worker1 gibi)

    def show_info(self):                   #class`a ait fonk: metod
        print(f"Name:{self.name}  Surname:{self.surname}  Age:{self.age}")


    @staticmethod
    def calculate_birth_year(workers):   #icine bir sey almak zorunda degil.
        return date.today().year - workers.age 



worker1 = workers("Ali", age=25)              
print(worker1.name, worker1.surname, worker1.age)    #age girmeyince ustte belirtilen "0" verecek. surname`i yapamadim ***

worker2 = workers("Ahmet", "Mehmet", 20)
print(worker2.name, worker2.surname, worker2.age)

worker1.show_info() 
worker2.show_info() 
print(workers.calculate_birth_year(worker1))

workers.show_info(worker1)       #ayni usttekilerle


#CLASS VARIABLES - INSTANCE VARIABLES 
print("++++++++++++++++++++++++")

class working_people:
    increase_rate = 1.1             #class variable
    employees = 0
    def __init__(self, name, salary):
        self.name = name            #instance variable (nesneye ait)
        self.salary = salary
        working_people.employees += 1 

    def give_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"        #instance method

    @classmethod
    def how_many_people(cls):
        return cls.employees
    
    @classmethod
    def make_a_string(cls, str_):
        name, age = str_.split("-")
        return cls(name, age)
    




print(working_people.employees)
working1 = working_people("Ali", 5000)
print(working_people.employees)
working2 = working_people("Ahmet", 6000)
print(working_people.employees)
working3 = working_people.make_a_string("Ayse-25")

print(working1.give_info())
print(working_people.how_many_people())

print(working1.__dict__)             #increase_rate degiskenini nesnede bulamayinca class`a bakiyor.
print(working_people.__dict__)



#        super().__init__(name, surname ....)   #ustteki classtan inherite yariyor. init icine tekrar
#        print(isinstance(...,...))     #bir nesne bir class`a ait bir ornek mi diye bakiyor true/false
#        print(issubclass(...,...))     #bir class baska class`in alt classi mi diye bakiyor true/false


#Dunder Methods / Magic Methods
#double underscore method: dunder

print(3 + 5)
print(int.__add__(3,5))

print("Ali", "Veli")
print(str.__add__("Ali","Veli"))

print([1,2,3] + [4,5,6])
print(list.__add__([1,2,3],[4,5,6]))

class MyList(list):
    def __add__(self, other):
        if len(self) != len(other):
            return "Can not be added."
        else:
            result = MyList()
            for i in range(len(self)):
                result.append(self[i] + other[i])

        return result
    
    def __sub__(self, other):
        if len(self) != len(other):
            return "Can not be done."
        else:
            result = MyList()
            for i in range(len(self)):
                result.append(self[i] - other[i])

        return result
    
    def __eq__(self, other):
        if sum(self) == sum(other):
            return True
        return False
    
    def __abs__(self):         #mutlak deger
        result = MyList()
        for i in self:
            if i >= 0:
                result.append(i)
            else:
                result.append(-1 * i)
        return result




list1 = MyList([1,2,3])
list2 = MyList([4,-5,6])

print(list1 + list2)
print(list1 - list2)
print(list1 == list2)
print(abs(list2))


#__str__ and __repr__
a = "Python"

print(str(a))
print(repr(a))        #`  ` ile yazdirir.

today = date.today()

print(today)
print(str(today))     #kullaniciya gostermek icin bu sekilde.
print(repr(today))    #datetime objesi oldugunu yazar. 

class Footballer:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}"
    
    def __repr__(self):
        return "repr is working"     #print str`yi calistirmayi tercih ediyor, yoksa repr yazdirir.

footballer1 = Footballer("Ali", "Veli", 25)

print(footballer1)   #class ve obje olarak yazdiriyor str tanimlamazsak
print(repr(footballer1)) 
        