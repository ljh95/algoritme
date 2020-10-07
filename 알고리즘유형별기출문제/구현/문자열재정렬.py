s = input()

sum = 0
new_s = []
for i in s:
    if (ord(i) < 65): # 숫자
        sum += int(i)
    else:
        new_s.append(i)

new_s.sort()
ss = ''
for i in new_s:
    ss+=i
print(ss+str(sum))