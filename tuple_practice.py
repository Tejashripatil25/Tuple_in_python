""""""

1.Reverse the following tuple. a= (10, 20, 30, 40, 50)
a = (10, 20, 30, 40, 50)
print(list(reversed(a)))
==================================================================
2.Access value 20 from the following tuple.  a= ("Orange", [10, 20, 30], (5, 15, 25))
a= ("Orange", [10, 20, 30], (5, 15, 25))
print(a[1][1])
==================================================================
3.Create a tuple with single item 50.
tup = 50,
print(tup)
print(type(tup))
==================================================================
4.Unpack the following tuple into 4 variables. a= (10, 20, 30, 40)
a= (10, 20, 30, 40)
w,x,y,z = (10, 20, 30, 40)
print(w)
print(x)
print(y)
print(z)
==================================================================
5.Swap the following two tuples. a= (11, 22), b= (99, 88)
a= (11, 22)
b= (99, 88)
a,b = b,a
print(a)
print(b)
==================================================================
6.Copy element 44 and 55 from the following tuple into a new tuple. tuple2: (44, 55)
tuple2 = (44, 55)
t1 = tuple2[0],tuple2[1]
print(t1)
=================================================================
7.Modify the first item (22) of a list inside a following tuple to 222. a=(11, [22, 33], 44, 55)
a = (11, [22, 33], 44, 55)
a[1][0]=222
print(a)
=================================================================
8.Counts the number of occurrences of item 50 from a tuple. a=(50, 10, 60, 70, 50)
a=(50, 10, 60, 70, 50)
print(a.count(50))
=================================================================
9.Assign the first element of the tuple to t1 on line 2. | t=(11, 100, 99, 1000, 999)
t=(11, 100, 99, 1000, 999)
t1 = t[0]
print(t1)
=================================================================
10.What's the index of 2? | t=(55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99)
t=(55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99)
print(t.index(2))
=================================================================
11.How many times does 777 occur? |
t = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 2, 6)
print(t.count(777))
=================================================================
12.What is the sum of all the numbers in the tuple? | t=(42, 1092, 11, 88, 65, 2, 6)
t = (42, 1092, 11, 88, 65, 2, 6)
print(sum(t))
=================================================================
13.What is the minimum value in the tuple? | t=(66, 555, 11, 101, 9, 1001)
t = (66, 555, 11, 101, 9, 1001)
print(min(t))
=================================================================
14.Write a statement to create an empty tuple named ‘T1’.
T1 = ()
print(T1)
print(type(T1))
=================================================================
15.Write the code to convert the given list L1 to tuple. L1 = [1, 2, 3, 4, 5]
L1 = [1, 2, 3, 4, 5]
t = tuple(L1)
print(t)
=================================================================
16.Write a code to create a tuple ‘T1’ containing first five even numbers.
T1 = (2,4,6,8,10)
print(T1)
=================================================================
17.Write a statement to create tuple T1 with single element.
t = (20,)
print(t)
print(type(t))
=================================================================
18.Swap two tuples in Python | tuple1 = (11, 22) and tuple2 = (99, 88)
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1,tuple2=tuple2,tuple1
print(tuple1)
print(tuple2)
=================================================================
19.Copy specific elements from one tuple to a new tuple | tuple1 = (11, 22, 33, 44, 55, 66)
expected tuple2: (44, 55)
tuple1 = (11, 22, 33, 44, 55, 66)
t1 = tuple1[3],tuple1[4]
print(t1)
=================================================================
20.Modify the tuple | tuple1 = (11, [22, 33], 44, 55) EXPECTED tuple1= (11, [222, 33], 44, 55)
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)
=================================================================
21.Write a program to accept five fruit name from the user and store it in a tuple ‘F1’.
f1 = input("Enter the fruit name:")
f2 = input("Enter the fruit name:")
f3 = input("Enter the fruit name:")
f4 = input("Enter the fruit name:")
f5 = input("Enter the fruit name:")
F1 = f1,f2,f3,f4,f5
list(F1).extend(F1)
print(tuple(F1))
=================================================================
22.Consider the following tuple and write the code for the following statements :
T1 = (12, 3, 45, ‘Hockey’, ‘Anil’, (‘a’, ‘b’)) |a. Display the first element of ‘T1’ |
b. Display the last element of ‘T1’ | c. Display ‘T1’ in reverse order.
d. Display ‘Anil’ from tuple ‘T1’ | e. Display ‘b’ from tuple ‘T1’
T1 = (12, 3, 45, 'Hockey', 'Anil', ('a', 'b'))
print(T1[0])#a.
t = list(T1)
t1 = t[::-1]
print(t1[0])#b
print(t1)#c
print(T1[4])#d
print(t1[0][1])#e
=================================================================
23.Write a program to accept three numbers from the user and insert it at the end of given Tuple T1.
 T1 = (23, 32, 4, 5, 2, 12, 23)
 T1 = (23, 32, 4, 5, 2, 12, 23)
fnum = int(input('Enter the first number:'))
snum = int(input('Enter the second number:'))
tnum = int(input('Enter the third number:'))
s1 = fnum,snum,tnum
t = list(T1)
t.extend(s1)
print(tuple(t))
=====================================================================
24.Write a program to print the frequency of a number accepted from the user in given tuple :
T1 = (12, 17, 18, 25, 19, 12, 18, 5)
s = int(input("Enter the number:"))
t = T1.count(s)
print(t)
====================================================================
25.Write a program in python to concatenate all the characters of given tuple.
T1 = (‘B’ , ‘O’, ‘O’, ‘K’) Expected OUTPUT : BOOK
T1 = ('B','O','O','K')
s = T1[0]+T1[1]+T1[2]+T1[3]
print(s)
print(type(s))
p = list(T1)
p1 = ''.join(p)
print(tuple(p1))
=====================================================================
26.Write a program to remove a number (accepted from the user) from the given tuple
T1 = (12, 15, 18, 21, 24, 27, 30)
T1 = (12, 15, 18, 21, 24, 27, 30)
num = int(input("Enter the number:"))
T = list(T1)
T.remove(num)
print(tuple(T))
====================================================================
27.Write one similarity between Tuples and String.
= Tuple and string both are immutable in nature,duplicates are allow in both cases
====================================================================
28.Write a program to accept roll number from user and display its detail from given tuple
Det = ((1, 'Amita', 'B'), (2, 'Sunita', 'C'), (3, 'Daya', 'A'))
roll_num = int(input("Enter the roll number:"))
c = 0
for i in range(3):
    if roll_num == Det[i][0]:
        print(Det[i])
        c = 1
======================================================================
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
        break
else:
    print("Record not found")
=======================================================================
# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')

# elements beginning to 2nd
print(my_tuple[:-7]) # prints ('p', 'r')

# elements 8th to end
print(my_tuple[7:]) # prints ('i', 'z')

# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
===========================================================================
