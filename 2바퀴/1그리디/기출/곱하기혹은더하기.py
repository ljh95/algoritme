s = input()
answer = int(s[0])
for i in range(1, len(s)):
    value = int(s[i])
    if answer == 0 or answer == 1 or value == 0 or value == 1:
        answer += value
    else:
        answer *= value
print("answer =", answer)