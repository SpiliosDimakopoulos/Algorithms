def KnuthMorrisPratt(p, t):
    q = CreateQueue()
    b = FindBorders(p)
    m = len(p)
    n = len(t)
    j = 0 

    for i in range(n):
        while j > 0 and p[j] != t[i]:
            j = b[j] 

        if p[j] == t[i]:
            j += 1 

        if j == m:
            q.Enqueue(i - j + 1)  
            j = b[j]  

    return q
