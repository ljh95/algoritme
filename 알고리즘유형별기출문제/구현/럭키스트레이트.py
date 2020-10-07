s = input()
mid_s = len(s)//2

front_s = s[:mid_s]
back_s = s[mid_s:]

count_f, count_b = 0, 0

for i in range(len(front_s)):
    count_f += int(front_s[i])
    count_b += int(back_s[i])

if count_f == count_b:
    print("LUCKY")
else:
    print("READY")
