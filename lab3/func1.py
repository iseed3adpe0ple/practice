import itertools
import math
import random
#Task 1
# a = int(input())
# def my_func(a):
#     return a*28.3495231
# print(my_func(a))



#Task 2
# a = int(input())
# def my_func(a):
#     return (5/9)*(a-32)
# print(my_func(a))

#Task 3
# def solve(numheads, numlegs):
#     x = (numlegs-4*numheads)/ -2
#     y = numheads - x
#     return int(x), int(y)
# print(solve(35, 94))

#Task 4
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# def is_prime(q):
#     if q == 1:
#         return 0
#     for i in range(2, int(q ** 0.5) + 1):
#         if q % i == 0:
#             return 0
#
#     return 1
# b = list(filter(is_prime, a))
# print(b)

#Task 5
# def per():
#     a = input()
#     p = set(itertools.permutations(a))
#     for i in p:
#         print(''.join(i))
# per()

#Task 6
# def func(s):
#     a = s.split(" ")
#     a = a[::-1]
#     s = " ".join(a)
#     return s
# print(func("are we ready"))

#Task 7
# def has_33(nums):
#     for i in range(len(nums)-1):
#         if(nums[i] == 3 and nums[i+1] == 3):
#             return 1
#     return 0
# print(has_33([1, 3, 1, 3]))

#Task 8
# def has_33(nums):
#     for i in range(len(nums)-2):
#         if(nums[i] == 0 and nums[i+1] == 0 and nums[i+1] == 7):
#             return 1
#     return 0
# print(has_33([1, 3, 1, 3]))

#Task 9
# def volume(r):
#     return 4/3*math.pi*(r**3)
# print(volume(6))

#Task 10
# def new_list(a):
#     b = []
#     for i in range(len(a)):
#         t = True
#         for j in range(i+1, len(a)):
#             if a[i] == a[j]:
#                 t = False
#         if(t):
#             b.append(a[i])
#
#     return b
# print(new_list([1, 112, 12, 1, 1, 2, 3, 2, 3]))

#Task 11
# def pal(s):
#     s1 = s[::-1]
#
#     if s == s1:
#         return True
#     else:
#         return False
# print(pal("asaa"))

#Task 12
# def histogram(a):
#     for i in a:
#         print("*"*i)
# print(histogram([1, 2, 3]))

#Task 13
def rand_num():
    b = random.randint(1, 100)
    a = int(input())
    while(a!=b):
        if(a < b):
            print("too low")
        elif a > b:
            print("too high")

        a = int(input())
    print("victory")
rand_num()