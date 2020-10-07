def solution(w,h):
    answer = 1
    g = gcm(w, h)
    _w = w//g
    _h = h // g
    k = _w + _h -1
    answer = (w*h) - (k*g)
    return answer

def gcm(a, b):
    big = max(a, b)
    small = min(a, b)

    while (big % small) != 0:
        r = big%small
        big = small
        small = r
    return small

w = 8
h = 12

print(solution(w, h))