n = int(input())
answer = 0
for k in range(n):
    s = input()
    arr = []
    flag = True

    for i in range(len(s)):
        if s[i] in arr:
            if s[i-1] != s[i]:
                flag = False
                break
        else:
            arr.append(s[i])
    if flag:
        answer += 1
    
print(answer)