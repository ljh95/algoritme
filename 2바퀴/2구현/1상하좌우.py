d = ['L', 'R', 'U', 'D']
dx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start = [1, 1]
n = int(input())
list_arr = input().split()

for s in list_arr:
    for i in range(len(d)):
        if d[i] == s:
            n_x = dx[i][0] + start[0]
            n_y = dx[i][1] + start[1]
            if n_x>0 and n_x<=n and n_y>0 and n_y<=n:
                start[0] = n_x
                start[1] = n_y

print(start[1], start[0])