class Node(object):
    left = None
    right = None
    value = ""


def getNode(strmath):
    a = Node()
    fist = strmath.find('(')
    en = strmath.rfind(')')
    if fist == 0 and en == len(strmath) - 1:
        strmath = strmath[1:-1]
    skobki = 0
    p = 0
    p1 = 0
    for i in range(len(strmath)):
        if strmath[i] == '(':
            skobki += 1
        elif strmath[i] == ')':
            skobki -= 1
        elif skobki > 0:
            pass
        elif strmath[i] in "-+":
            p = i
        elif strmath[i] in "*/":
            p1 = i
    if p == 0:
        if p1 == 0:
            a.value = strmath
            return a
        else:
            p = p1
    a.value = strmath[p]
    a.left = getNode(strmath[:p])
    a.right = getNode(strmath[p+1:])
    return a


def stupid_math(a, b, c):
    if b == "/":
        return a/c
    elif b == "*":
        return a*c
    elif b == "-":
        return a-c
    elif b == "+":
        return a+c


def mathNode(arifm):
    if arifm.value in "/*-+":
        return stupid_math(int(mathNode(arifm.left)), arifm.value, int(mathNode(arifm.right)))
    else:
        return arifm.value


a = input()
print(mathNode(getNode(a)))