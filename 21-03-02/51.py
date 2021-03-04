def corect_bracks(bracks):
    stack = []
    for i in bracks:
        if i in "([{<":
            stack.append(i)
        elif i in ")]}>":
            a = stack[-1] + i
            if a in "()[]{}<>":
                stack.pop()
            else:
                return 0
        else:
            pass
    return 1

a = input()
if corect_bracks(a):
    print("corect")
else:
    print("not corect")
