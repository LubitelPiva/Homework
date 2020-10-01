from array import *

name = ["AAA", "AAB", "AAC", "AAD", "AAE", "AAF", "AAG", "AAI", "AAJ", "AAK"]
surname = ["AAA", "AAB", "AAC", "AAD", "AAE", "AAF", "AAG", "AAI", "AAJ", "AAK"]
birtday = []
for i in range(10):
    birtday.append(str(i % 12 % 30 + 1) + '.' + str(i // 30 % 12 + 1) + '.' + str(i // 30 // 12))

def watch(b):
    if b > len(name) - 1:
        print("error id")
        return
    print(name[b])
    print(surname[b])
    print(birtday[b])

def plus(a, b, c):
    name.append(a)
    surname.append(b)
    birtday.append(c)

def dellit(a):
    if a > len(name) - 1:
        print("error id")
        return
    name.pop(a)
    surname.pop(a)
    birtday.pop(a)

def sort(a):
    for i in range(len(name)):
        for k in range(i + 1, len(name)):
            if a == "name":
                if name[i] > name[k]:
                    name[i], name[k] = name[k], name[i]
                    surname[i], surname[k] = surname[k], surname[i]
                    birtday[i], birtday[k] = birtday[k], birtday[i]
            elif a == "surname":
                if surname[i] > surname[k]:
                    name[i], name[k] = name[k], name[i]
                    surname[i], surname[k] = surname[k], surname[i]
                    birtday[i], birtday[k] = birtday[k], birtday[i]
            elif a == "birtday":
                if birtday[i] > birtday[k]:
                    name[i], name[k] = name[k], name[i]
                    surname[i], surname[k] = surname[k], surname[i]
                    birtday[i], birtday[k] = birtday[k], birtday[i]
            else:
                print("this table haven't such a column")

while "true":
    task = input("choose a task:print, append, dellit, sort\n")
    if task == "print":
        i = int(input("wrait id:"))
        watch(i)
    elif task == "append":
        a, b, c = input("wrait info:").split(' ')
        plus(a, b, c)
    elif task == "dellit":
        i = int(input("wrait id:"))
        dellit(i)
    elif task == "sort":
        a = input("choose a sort:name, surname, birtday\n")
        sort(a)
    else:
        print("error")
    print("\n")