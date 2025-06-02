    #List Comprehension
    #Uzun kodlari tek bir kodda toplamaya yariyor.

#Example 1
squares = []
for i in range(1,101):
    squares.append(i**2)
print(squares)
#instead:
squares2 = [i**2 for i in range(1,101)]
print(squares2)


#Example 2
remainders5 = [x**2 % 5 for x in range(1,101)]
print(remainders5)
remainders11 = [x**2 % 11 for x in range(1,101)]
print(remainders11)


#Example 3
movies = [("Citizen Kane", 1941), ("Gattaca", 1997), ("Spirited Away", 2001)]

pre2k = [title for (title, year) in movies if year < 2000]
print(pre2k)


#Example 4
v = [2, -3, 1]
4 * v    #olmaz (art arda yazar + + +)

w = [4*x for x in v]
print(w)


#Example 5 - Cartesian Product
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)


#Example 6
from time import time

start = time()
[n**2 for n in range(1,1000000)]
end = time()
print("List comp run time:", end - start)

start = time()
squares = []
for n in range(1,1000000):
    squares.append(n**2)
end = time()
print("Loop + append time:", end - start)
