class Node(object):
    left = None
    right = None
    value = ""


def getNode(strmath):
    a = Node()
    fist = strmath.find('(')
    en = strmath.rfind(')')
    if fist == 0 and en == len(strmath)-1:
        b = strmath[1:-2]
        fist = strmath.find('(')
        en = strmath.rfind(')')
    b = strmath[:fist] + strmath[en+1:]
    if '+' in b or '-' in b:
        p = max(b.find("+"), b.find("-"))
    elif '*' in b or '/' in b:
        p = max(b.find("*"), b.find("/"))
    else:
        a.value = b
        return a
    a.value = b[p]
    a.left = getNode(b[:p])
    a.right = getNode(b[p+1:])
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
    print(arifm.value)
    if arifm.value in "/*-+":
        return stupid_math(int(mathNode(arifm.left)), arifm.value, int(mathNode(arifm.right)))
    else:
        return arifm.value


a = input()
print(mathNode(getNode(a)))