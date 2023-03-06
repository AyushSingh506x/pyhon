import colorama as c

from colorama import Fore, Back , Style
c.init(autoreset=True)
# print(Fore.RED + 'hello')



order = input("enter the order of the sequence: ")
if (order != "s" and order != "r"):
    raise ValueError(Fore.RED +"wrong input u can only enter 's' or 'r'")
pos = input("enter the position of the sequence: ")
if (pos != "v" and pos != "h"):
    raise ValueError (Fore.RED + """wrong input u can only enter "v" or "h"' """)
jump=int(input("enter the value u wanna jump: "))
start=int(input("enter the starting point: "))
n = int(input("enter the range of the sequence: "))

if(order=="r"):
    if(n<start):
        raise ValueError(f"for reverse condition n should be greater then start")

if(order=="s"):
    if(n<start):
        raise ValueError(" for sequence condition n should be start")

if (order == "r"):
    if (pos == "h"):
        for i in range(n, start,-jump):
            print(i, end=" ")
        # elif(order=="r"):
    elif (pos == "v"):
        for i in range(n, start,-jump):
            print(i)
elif (order == "s"):
    if (pos == "h"):
        for i in range(start, n,jump):
            print(i, end=" ")
# elif(order=="s"):
    elif (pos == "v"):
        for i in range(start, n,jump):
            print(i)


