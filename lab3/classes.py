import math

#Task 1
# class my_class:
#     def getString(self, s):
#         self.s = s
#
#     def pringString(self):
#         print(self.s)
#
# p = my_class()
# p.getString("hi")
# p.pringString()


#Task 2 & 3
# class Shape:
#     def __init__(self, length):
#         self.length = length;
#     def area(self):
#         print(self.length)
#
# class Square(Shape):
#     def area(self):
#         print(self.length**2)
#
# p = Square(10)
# p.area()
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         Shape.__init__(self, length)
#         self.width = width
#     def area(self):
#         print(self.length*self.width)
#
# p1 = Rectangle(10, 3)
# p1.area()

#Task 4
# class Point:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def show(self):
#         print(self.x1, self.y1)
#         print(self.x2, self.y2)
#
#     def move(self, a1, b1, a2, b2):
#         self.x1 = a1
#         self.y1 = b1
#         self.x2 = a2
#         self.y2 = b2
#
#     def dist(self):
#         print(math.sqrt(self.x2-self.x1)**2+(self.y2-self.y1)**2)
#
# p = Point(2, 2, 8, 7)
# p.show()
# p.move(4, 4, 5, 6)
# p.show()
# p.dist()

#Task 5
# class Account:
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0
#
#     def deposit(self, m):
#         self.m = m
#         self.balance += m
#
#     def withdrow(self, n):
#         self.n = n
#         if(self.balance-n<0):
#             print("Account cannot be overdrawn")
#             pass
#         self.balance -= n
#
# p = Account("dan")
# p.deposit(100)
# p.withdrow(30)
# p.withdrow(1000)

#Task 6
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
def is_prime(q):
    if q == 1:
        return 0
    for i in range(2, int(q ** 0.5) + 1):
        if q % i == 0:
            return 0

    return 1
b = list(filter(is_prime, a))
print(b)