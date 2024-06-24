def bi(t):
    o=len(t)
    l=[]
    for i in range (o):
        t2=t[i][::-1]
        for j in range(i,o):
            if t[j]==t2:
                #l+=t[i], this line or next line both are same
                l+=t2,
    return(l)
print(bi([(1,1,2,1),(3,4,3),(3,5),(4,3),(5,3,5),(2,2)]))
