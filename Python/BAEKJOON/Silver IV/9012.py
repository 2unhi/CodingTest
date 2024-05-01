T = int(input())

for _ in range(T):
    stack = []
    g = input()

    for i in g:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if len(stack) == 0:
                stack.append(")")
                break
            else:
                stack.pop()

    if(len(stack) == 0):
        print("YES")
    else:
        print("NO")