s = input()
stack = []
flag = True
n = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    elif s[i] == ")":
        if not stack:
            flag = False
            n = i
            break

        open_bracket = stack.pop()
        if open_bracket == "(" and s[i] == ")":
            continue
        flag = False
        break

if flag and len(stack) == 0:
    print("It's correct bracket sequence")
else:
    print(f"It isn't correct bracket sequence\n{n + 1}: {s[n]}")
