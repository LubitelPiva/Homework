def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = []
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token[0] in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while len(opStack) != 0 and (prec[opStack[-1]] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.append(token)

    while len(opStack) != 0:
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def stupid_math(a, b, c):
    if b == "/":
        return a/c
    elif b == "*":
        return a*c
    elif b == "-":
        return a-c
    elif b == "+":
        return a+c

def smart_math(a):
    a = infixToPostfix(a).split()
    s = []
    for i in a:
        if i in "/*-+":
            fist = s.pop()
            second = s.pop()
            s.append(stupid_math(second, i, fist))
        else:
            s.append(float(i))
    return s[0]


a = input()
print(smart_math(a))