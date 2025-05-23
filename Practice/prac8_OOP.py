     #OBJECT ORIENTED PROGRAMMING
#class: Ortak ozellikleri olan nesneleri gruplandiriyoruz. class`tan uretilmis ornek(instance) 

class workers:
    def __init__(self,name,surname,age=0):   #initialize fonk, baslatmak olusturmak icin kullaniyoruz.
        
        self.name = name
        self.surname = surname
        self.age = age                     #self = olusturulan degisken (worker1 gibi)

    def show_info(self):                   #class`a ait fonk: metod
        print(f"Name:{self.name}  Surname:{self.surname}  Age:{self.age}")

    



worker1 = workers("Ali", "Veli")              
print(worker1.name, worker1.surname, worker1.age)    #age girmeyince ustte belirtilen "0" verecek. surname`i yapamadim ***

worker2 = workers("Ahmet", "Mehmet", 20)
print(worker2.name, worker2.surname, worker2.age)

worker1.show_info() 
worker2.show_info() 

workers.show_info(worker1)       #ayni usttekilerle

