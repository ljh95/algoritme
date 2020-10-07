def primes_up_to(n: int) -> [int]: 
    seive = [False, False] + [True] * (n-1) 
    for (i, e) in enumerate(seive): 
        if e:
            k = i * 2 
            while k <= n: 
                seive[k] = False 
                k += i 
    return [x for (x, y) in enumerate(seive) if y ]

print(primes_up_to(30))

