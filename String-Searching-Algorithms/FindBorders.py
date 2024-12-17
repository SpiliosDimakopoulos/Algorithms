def FindBorders(p):
    m = len(p)
    b = [0] * (m + 1) 
    j = 0 

    b[0] = j 
    b[1] = j 

    for i in range(1, m):
        while j > 0 and p[j] != p[i]:
            j = b[j]

        if p[j] == p[i]:
            j += 1
            
        b[i + 1] = j

    return b
