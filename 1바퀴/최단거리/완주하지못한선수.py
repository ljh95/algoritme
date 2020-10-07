def solution(participant, completion):
    p = dict()
    for i in participant:
        if i not in p:
            p[i] = 0
        else:
            p[i] = p[i]+1
    for i in completion:
        if p[i]>0:
            p[i]-=1
        else:
            del p[i]
    ll = list(p)
    return str(ll[0])
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))