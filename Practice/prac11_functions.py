# Ic Ice Fonksiyonlar:
def calculations(x):
    def square(a):
        return a ** 2
    def square_root(a): 
        return a ** 0.5
    square = square(x)               #fonk.u yazdiktan sonra tekrar cagirmayi unutmamak lazim.
    square_root = square_root(x)
    return f"Square: {square}, Square Root: {square_root}"   #dis fonk.a return etmemiz gerekiyor sonuc almak icin.
print(calculations(9))

def sum_multiple(*args):
    def adding(tuple):
        return sum(tuple)
    def multiplying(tuple):
        x = 1 
        for i in tuple:
            x *= i 
        return x 
    return f"Sum: {adding(args)} Multiply: {multiplying(args)}"
print(sum_multiple(2,4,5,8))


print("*************************************************")
# Fonksiyonlardan Fonksiyon Dondurme: 
def func(x):
    return x * x

a = func(3)
b = func 
print(b)      #func oldugunu yazdirir. 
print(b(5)) 

def choose_calculations(calculation):
    def adding(*args):
        add = 0
        for arg in args:
            add += arg
        return add
    def multiplying(*args):
        multiply = 1 
        for arg in args:
            multiply *= arg
        return multiply
    def average(*args):
        return sum(args) / len(args)

    if calculation == "adding":
        return adding
    elif calculation == "multiplying":
        return multiplying
    elif calculation == "average":
        return average
    
sum_func = choose_calculations("adding")
multiply_func = choose_calculations("multiplying")
average_func = choose_calculations("average")

print(sum_func(1,2,3,4))
print(multiply_func(3,4,5))
print(average_func(2,4,6,8))

def people(person): 
    def jobs(job):
        return f"{person} is a {job}."
    return jobs

a = people("Ali")
b = people("Ahmet")

print(a("Doctor"))
print(b("Lawyer"))


print("*************************************************")
# Fonksiyonlara Parametre Olarak Fonksiyon Gondermek:
def adding(x,y):
    return x + y
def multiplying(x,y):
    return x * y

def calculating(func,a,b):
    return func(a,b)

print(calculating(adding,3,5))

list1 = [1,2,3,4,5]
list2 = [1,3,5,8,9,11]

def square(x):
    return x * x 
def cube(x):
    return x * x * x 

def map_func(func,list):
    results = []
    for i in list:
        results.append(func(i))
    return results

print(map_func(square,list2))
print(map_func(cube,list1))

print("*************************************************")

# property/ setter/ deleter:
@property
def celsius(self):
    print("Getting celsius")
    return self._celsius  #private/ internal value that stores the actual temperature value.
                         #it is to use inside the class.
                         # Read the real data

@celsius.setter
def celsius(self, value):
    print("Setting celsius")
    if value < -273.15:
        raise ValueError("Temperature can't go below absolute zero (-273.15°C).")
    self._celsius = value # Update the real data

@property
def fahrenheit(self):
    return (self._celsius * 9/5) + 32

@fahrenheit.setter
def fahrenheit(self, value):
    self.celsius = (value - 32) * 5/9  # Reuse the celsius setter for validation

@fahrenheit.deleter
def fahrenheit(self):
    print("Deleting temperature...")
    del self._celsius

print("*************************************************")

# Map Func.
#Square Numbers
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)

#Convert strings to uppercase
names = ['alice', 'bob', 'charlie']
upper_names = list(map(str.upper, names)) #first the func, then the list
print(upper_names)

#Clean and convert data
raw_data = ['1', '2', ' 3 ', '4']
cleaned = list(map(lambda x: int(x.strip()), raw_data)) 
print(cleaned)

#Extract fields from a list of dicts
people = [
{"name": "Alice", "age": 30},
{"name": "Bob", "age": 24},
{"name": "Charlie", "age": 35}
]

names = list(map(lambda person: person["name"], people))
print(names)
#the same with list comprehension
names = [person["name"] for person in people]