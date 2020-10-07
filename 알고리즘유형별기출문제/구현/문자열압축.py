# s = input()
s = 'ababcdcd'
s = 'aabbaccc'
s = 'ababcdcdababcdcd'
s = 'abcabcdede'
s = 'abcabcabcabcdededededede'
s = 'xababcdcdababcdcd'
result = len(s)
for step in range(1, len(s)//2+1):
    end = step
    new_str = ''
    count = 1
    for i in range(0, len(s), step):
        front_str = s[i:i + step]
        back_str = s[i + step:i + 2*step]
        if front_str == back_str:
            count += 1
            end += step
        else:
            if count > 1:
                new_str += str(count)+ s[i:i+step]
            else:
                new_str += s[i:i+step]
            end += step
            count = 1
    
    result = min(result, len(new_str))

print(result)