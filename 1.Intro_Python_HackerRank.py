if __name__ == '__main__':
    ven="Hello, World!"
    print(ven)

print("________________________________ if")

#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    if n%2 != 0:
        print("Weird")
    else:
        if n>=2 and n<=5:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")

print("__________________________________ Arithmetic")

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)

print("________________________________ Divison")

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)

print("________________________________ Loops")

if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)
        
print("________________________________ Function")

def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))

print("______________________________ Print Function")

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')

print("______________________________ ")

