class Node(object):
    left = None
    right = None
    value = ""


def getNode(strmath):
    a = Node()
    if '+' in strmath or '-' in strmath:
        p = max(strmath.find("+"), strmath.find("-"))
    elif '*' in strmath or '/' in strmath:
        p = max(strmath.find("*"), strmath.find("/"))
    else:
        a.value = strmath
        return a
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