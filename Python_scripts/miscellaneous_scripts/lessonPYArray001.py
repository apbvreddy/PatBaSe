from array import *
'''
#String Array
dogs = ["Spot", "Max", "Sam", "Charlie", "Cooper", "Duke", "Bear", "Buddy", "Milo", "Murphy"]
print(dogs)
dogs.append("Wrigley")
print(dogs)
dogs.insert(1, "Wrigley")
print(dogs)
x = dogs[0]
print(x)
dogs[0] = "Jack"
print(dogs)
dogs.pop(9)
print(dogs)
dogs.remove("Duke")
print(dogs)
x = len(dogs)
print(x)


#Number Array
numbers = [5, 13, 25, 2, 98, 56, 4, 8]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
dogs = ["Spot", "Max", "Sam", "Charlie", "Cooper", "Duke", "Bear", "Buddy", "Milo", "Murphy","Sam"]
x = dogs.count("Sam")
print(x)
'''

#2D Arrays
#temperatures = [[52, 60, 66, 63], [50, 58, 62, 60], [53, 61, 67,64], [51, 59, 65, 62]]
#print(temperatures)
T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
print(T[0])
print(T[1][2])
'''
for r in T:
   for c in r:
      print(c,end = " ")
   print()

T.insert(2, [0,5,11,13,6])

for r in T:
   for c in r:
      print(c,end = " ")
   print()

T[2] = [11,9]
T[0][3] = 7
for r in T:
   for c in r:
      print(c,end = " ")
   print()
'''


del T[3]

for r in T:
   for c in r:
      print(c,end = " ")
   print()




