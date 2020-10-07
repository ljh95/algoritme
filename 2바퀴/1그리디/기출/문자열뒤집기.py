s = input()
count = 0
for i in range(len(s) - 1):
    value = int(s[i])
    n_value = int(s[i+1])

    if value != n_value:
        count+=1
count-=count//2
print("answer =", count)