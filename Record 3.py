def lseq(l):
    a=0
    l2=[l[0]]
    l3=[]
    for i in range(1,len(l)):
        if l[i]==l[i-1]+1:
            l2+=l[i],
        else:
            l3+=l2,
            l2=[l[i],]
    l3+=l2,
    for i in l3:
        if len(i)>a:
            a=len(i)
    return(a)
print(lseq([1,2,3,4,3,4,5,6,7,9,8,4,1,2,3,4,5,6]))

