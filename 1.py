# Python tutorial Computer Science Circles
# Created: 8/3/2021 
# Anyone  

# print('hello world') 
# print("Bonjour, tout le monde!")
# print(3+4)
# print(3*4)
# print(3**4)
# cat=5
# print(cat)
# cat=6
# print(cat)
# people = 10
# heads = people
# shoulders = people * 2
# knees = people * 2
# toes = people * 10
# print(people, heads, shoulders, knees, toes)
# x = 1
# y = 2
# print(x, y)
# # z = x
# # x = y
# # y = z
# # print(x, y)
# x, y = y, x
# print(x, y)
# print("Hello")
# username ='Joe' 
# print(username)

# x = max(max(16, 7), min(8, 70), max(80, 90))
# print(x)

# maximumweightfirst = min(a, b, c)
# maximumweightsecond = min(d, e)
# maximumweight = max(maximumweightfirst, maximumweightsecond)
# print(maximumweight)

# min(max(10, balance*0.021), balance)

# print(sorted((70, 90, 80), reverse=True)) # reverse default parameter

# print('A double-quote\'s escaped using a backslash, e.g. \\"')

# print("blue" * 20)

# x = float("3.4")
# print(x + 1)
# y = int(x)
# print(y)

# inputStr = 15
# a = float(inputStr) ** 2 
# print(int(a / 100))

# x = input("please input a number:")
# print("The number is", x)

# pancakes = int(input())
# if pancakes > 3:
#     print("Yum!")
# else:
#     print("Still hungry")

# print(not(2 != 1))

# x = int(input())
# if x > 0:
#     print("Positive")
# elif x < 0:
#     print("Negative")
# else:
#     print("Zero")

# age = int(input())
# if age >= 18:
#     print('You can vote')
# else:
#     if age >= 0:
#         print('Too young to vote')
#     else:
#         print('You are a time traveller')

# print(35*0.01)

# n = int(input('how many timbits do you need'))
# largebox = int(n / 40)
# n = n - 40 * largebox
# price = 0
# price = price + 6.19 * largebox
# midbox = int(n / 20)
# n = n - 20 * midbox
# price = price + 3.39 * midbox
# smallbox = int(n / 10)
# n = n - 10 * smallbox
# price = price + 1.99 * smallbox
# price = price + 0.2 * n
# print('You need buy', largebox, 'largebox')
# print('You need buy', midbox, 'midbox')
# print('You need buy', smallbox, 'smallbox')
# print('You need buy', n, 'individual')
# print('Total price is', price ,'$')

# print('magic'[len('magic')-1])

# mystring = input()
# print(mystring[1:(len(mystring)-1)])

# mystring = input()
# print(mystring[len(mystring)-1] + mystring[1:len(mystring)-1] + mystring[0])

# char = input()
# if ord(char) == 90:
#     print(chr(65))
# else:
#     print(chr(ord(char)+1))

# mystr = input()
# print(mystr[1:len(mystr)] + mystr[0] + 'ay')

# n = str(input())
# print(n + ',' +  n + ',' + 'bo-b'  + n[1:len(n)])
# print('banana-fana fo-f' + n[1:len(n)])
# print('fee-fi-mo-m' + n[1:len(n)])
# print(n + '!')

# print(6 % 5)

# n = int(input())
# print(n // 12)
# print(n % 12)

# a = int(input())
# b = int(input())
# if a % b == 0:
#     print('divisible')
# else:
#     print('not divisible')

# import math
# print(math.tan(math.pi / 4))

# import math
# r = float(input())
# print(math.pi * (r ** 2))

# import math
# a = float(input())
# b = float(input())
# print(math.sqrt(a * b))

# print(-10 // 3, int(-10 / 3))

# a = int(input())
# b = int(input())
# c = int(input())
# print((a + b) * c)

# h = float(input())
# print(30.48 * h)

# import math
# v = float(input())
# t = (v - math.sqrt(v ** 2 - 4 * (-4.9) * 11000)) /(2* (-4.9))
# print(t)

# time = 1
# while time <= 10:
#     print(time)
#     time += 1 
# print('Blastoff!')

# for mychar in 'watermelon':
#     print(mychar)

# n = int(input())
# for i in reversed(range(1, n+1)):
#     X = 0
#     for j in range(i):
#         X = (X*10)+1
#     print(X)

# n = int(input())
# for i in range(1, n):
#     if i ** 2 >= n:
#         break
#     print(i ** 2)

# counter = 0
# while True:
#   lineIn = input()
#   if lineIn == 'END':
#     break
#   if lineIn == 'SKIP':
#     continue
#   counter = counter + 1
#   print('line', counter, '=', lineIn)

# n = int(input())
# for a in range(1, n + 1):
#     for b in reversed(range(1, n + 1)):
#         if a * b == n:
#             print(a, 'times', b, 'equals', n)

# n = int(input())
# for a in range(1, n + 1):
#     for b in reversed(range(1, n + 1)):
#         if a * b != n:
#             continue
#         print(a, 'times', b, 'equals', n)

# S = input()
# for i in range(len(S)):
#     if S[i] == '+':
#         a = int(S[:i])
#         b = int(S[i+1:])
#         print(a + b)

# needle = input()
# haystack = input()
# counter = 0
# for i in range(len(haystack) - len(needle)+1):
#     s = haystack[i:i+len(needle)]
#     if s == needle:
#         counter += 1
# print(counter)

# import math
# L = float(input())
# A = float(input())
# for T in range(0, 10):
#     X = L * math.cos(A * math.cos(T * math.sqrt(9.8 / L))) - L * math.cos(A)
#     print(X)

# width = int(input())
# while True:
#     lineIn = input()
#     if lineIn == 'END':
#         break
#     x = width - len(lineIn)
#     y = int(x / 2) if x % 2 == 0 else int(x / 2 + 1)
#     print('.' * y + lineIn + '.' * int(x / 2))

# t = input()
# d = int(input())
# a, b = t.split(':')
# a = int(a)
# b = int(b)
# c = int((b + d) / 60)
# e = int((a + c) % 24)
# f = int((b + d) % 60)
# print("{:02d}:{:02d}".format(e, f) )

# for i in range(32, 128, 16):
#     line1 = 'chr:'
#     line2 = 'asc:'
#     for j in range(16):
#         line1 += "{:>3c} ".format(i+j)
#         line2 += " {:<3d}".format(i+j)
#     print(line1)
#     print(line2)

# for i in range(32, 128, 16):
#     for j in range(16):
#         print(j, end=' ')
#     print(i)      

# x=int(input())
# if x >= 0:
#     print(x)
# else:
#     print(-x)

# x = int(input())
# if x == 1:
#     print(str(x) + 'st')
# elif x == 2:
#     print(str(x) + 'nd')
# elif x == 3:
#     print(str(x) + 'rd')
# else:
#     print(str(x) + 'th')

# letter = input()
# if ord(letter[0]) > 64 and ord(letter[0]) <= 90:
#     print(ord(letter[0])-64)
# else:
#     print('invalid')

# def repeatedPrint(string, repetitions):   # no returns in this function
#   for i in range(0, repetitions):
#     print(string)

# repeatedPrint('Hello, world!', 3)

# def cube(n):
#   return n ** 3

# def rectanglePerimeter(width, height):
#   return width * 2 + height * 2

# def lowerChar(char):
#   if ord(char) > 64 and ord(char) <= 90:
#     x = ord(char) + 32
#     return chr(x)
#   else:
#     return char
# def lowerString(string):
#   result = ''
#   for i in string:
#     result = result + lowerChar(i)
#   return result

# def xi(value):
#   global red
#   red = value
# red = 'blue'
# xi(input())
# print(red)

# import math
# def hypotenuse(a, b):
#   c = math.sqrt(a ** 2 + b ** 2)
#   return c
# def rightTrianglePerimeter(a, b):
#   return a + b + hypotenuse(a, b)

# def distance2D(x1, y1, x2, y2):
#   a = x1 - x2
#   b = y1 - y2
#   return hypotenuse(a, b)

# def trianglePerimeter(xA, yA, xB, yB, xC, yC):
#   a = distance2D(xA, yA, xB, yB)
#   b = distance2D(xA, yA, xC, yC)
#   c = distance2D(xB, yB, xC, yC)
#   return a + b + c

# for i in range(17, 98, 10):
#     print(i)

# mylist = [1, 2 ,3 ,4 ,5]
# for i in range(len(mylist)):
#     print(mylist[i])

# def middle(L):
#     return L[len(L) // 2]

# def naturalNumbers(n): 
#     return [i for i in range(1, n+1)]
# n = int(input())
# print(naturalNumbers(n)) 

# def isPalindrome(S):
#     for i in range(len(S)):
#         if S[i] != S[-i-1]:
#             return False
#     return True

# def prod(L):
#     s = 1
#     for i in L:
#         s = s * i
#     return s

# def replace(l, X, Y):
#     while X in l:
#         z = l.index(X)
#         l.remove(X)
#         l.insert(z, Y)

# def postalValidate(S):
#     S = S.replace(' ', '')
#     if len(S) < 2 or len(S) % 2 != 0:
#         return False
#     for i in range(0, len(S)-1, 2):
#         if not S[i+1].isdigit() or not S[i].isalpha():
#             return False
#     return S.upper()

# def getBASIC():
#     linein = []
#     while True:
#         a = input()
#         linein.append(a)
#         if 'END' in a.split():
#             return linein

# def findLine(prog, target):
#     for i in prog:
#         if target in i.split()[0]:
#             return(prog.index(i))

# def execute(prog):
#   location = 0
#   a = [False] * len(prog)
#   while True:
#     if location==len(prog)-1: return "success"
#     if a[location] == True: return 'infinite loop'
#     a[location] = True
#     T = prog[location].split()[-1]
#     location = findLine(prog, T)

# def countdown(n):
#   if n == 0:
#     print('Blastoff!')
#   else:
#     print(n)
#     countdown(n - 1)

# countdown(5)

# def digitalSum(n):
#     if n < 10:
#         return n
#     else:
#         digitalSum(n // 10)
#         a = 0
#         a = a + n % 10
#     print(a)
     
# print(digitalSum(6364))

# temp = input()
# if temp[len(temp)-1] == 'C':
#     c = float(temp[:len(temp)-1])
#     f = str(c * 9 / 5 + 32)
#     print(f + 'F')
# if temp[len(temp)-1] == 'F':
#     f = float(temp[:len(temp)-1])
#     c = str((f - 32) * 5 / 9)
#     print(c + 'C')

# def check(S):
#     if not len(S) == 19:return False
#     for i in range(4, 16, 5):
#         if not S[i] == ' ':return False
#     S = S.split(' ')
#     S = str(S[0]) + str(S[1]) + str(S[2]) + str(S[3])
#     if not S.isdigit():return False
#     x = 0
#     for j in range(16):
#         x = x + int(S[j])
#     if  x % 10 == 0:return True
#     else:return False
# print(check(''))
#How to conbine a list into a string


# poem = []
# while True:
#     S = input()
#     S = S.lower()
#     word = S.split()
#     poem = poem + word
#     if S == '###':
#         break
# counter = [0] * len(poem)
# for i in range(len(poem)):
#     for j in poem:
#         if poem[i] == j:
#             counter[i] = counter[i] + 1
# x = max(counter)
# y = counter.index(x)
# print(poem[y])

# def choose(n, k):
#     n = int(n)
#     k = int(k)
#     numerator = []
#     denominator = []
#     for i in range(n - k + 1, n + 1):
#         numerator = numerator + [i]
#     for j in range(1, k+1):
#         denominator = denominator + [j]
#     multi = 1
#     for k in range(0, k):
#         multi *= numerator[k] / denominator[k]
#     return multi
# print(choose(4, 2))


# def checkword(origin, S):
#     origin = origin.split(' ')
#     for i in range(len(origin)):
#         l = []
#         for m in origin[i]:
#             l += [m]
#         for j in range(len(l)):
#             a = ord(l[j]) - S
#             if a < 65:
#                 a = 91 - 65 + a
#             l[j] = chr(a)
#         newl = ''
#         for n in range(len(l)):
#             newl += str(l[n])
#         origin[i] = newl
#     final = ''
#     for k in range(len(origin)):
#         if k > 0:
#             final += ' ' + origin[k]
#         else: final += origin[k]
#     return final

# def checkgoodness(l):
#     letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
#     goodness = 0
#     for i in l:
#         goodness += letterGoodness[ord(i) - 65]
#     return goodness


# origin = input()
# origin = origin.split()
# final = [''] * len(origin)
# for i in range(len(origin)):
#     storage_g = [0] * 27
#     storage_l = [''] * 27
#     for S in range(27):
#         l = checkword(origin[i], S)
#         g = checkgoodness(l)
#         storage_g[S] = g
#         storage_l[S] = l
#     x = max(storage_g)
#     y = int(storage_g.index(x))
#     final[i] = storage_l[y]
# op = ''
# for j in range(len(final)):
#     if j > 0:
#         op += ' ' + final[j]
#     else: op += final[j]
# print(op)

# a = ' '.join(['my', 'name', 'is'])
# print(a)

# def countdown(n):
#   print('Entering countdown(',n,')')
#   if n == 0:
#     print('Blastoff!')
#   else:
#     print(n)
#     countdown(n - 1)
#     print('after countdown', n)
#   print('Exiting from countdown(',n,')')

# limit = int(input())
# countdown(limit)

# def digitalSum(n):
#     if n < 10:return n
#     else: return n % 10 + digitalSum(n // 10)

# n = str(input())
# a = 0
# for i in n:
#     a += int(i)
# print(a)

# def hailstone(n):
#     print(n)
#     if n == 1:return 1
#     if n % 2 == 0:
#         hailstone(int(n / 2))
#     else:
#         hailstone(3 * n + 1)

# def nestedListContains(NL, target):
#     for j in NL:
#         if not isinstance(j, int):
#             if not nestedListContains(j, target):
#                 continue
#             else: return True
#         if target == j:
#                 return True
#     return False
# print(nestedListContains([[9, 4, 5], [3, 8]], 3))

# oldsize = ['my', 1, 2]
# newsize = oldsize
# newsize[1] = 2
# print(oldsize)
# print(newsize)

# oldsize = 12800
# newsize = oldsize
# newsize *= 2
# print(oldsize)
# print(newsize)

# True False  False False
# True False  True  False

# import copy
# sample = [1, [2, 3]]
# sample1 = copy.copy(sample)
# sample2 = copy.deepcopy(sample)
# sample1[1][0] = 4
# print(sample)
# print(sample1)
# print(sample2)

# isPrime = [False] + [False] + [True] * 999999
# for n in range(2,1000001):
#     for D in range(2, n):
#         if (D * D > n): 
#             isPrime[n] = True
#             break
#         if n % D == 0:
#             isPrime[n] = False
# print(isPrime)

# import math
# isPrime = [False] + [False] + [True] + [False] + [True] + [True] * 999996
# for n in range(2,1000001):
#     if n % 2 == 0 or n % 5 == 0: 
#         isPrime[n] = False
#         continue
#     for D in range(2, int(math.sqrt(n) + 1)):
#         if n % D == 0:
#             isPrime[n] = False
#             break
# for i, j in enumerate(isPrime):
#     if j:
#         print(i)





    

       
    





