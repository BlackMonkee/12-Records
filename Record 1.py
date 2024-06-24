def seq(s):
    t=list(s.split('-'))
    o=len(t)
    s=''
    for i in range (o-1):
        for j in range(o-1):
            if t[j]>t[j+1]:
                t[j],t[j+1]=t[j+1],t[j]
    s='-'.join(t)
    return(s)
st=input('- ')
print(seq(st))
#print(seq("red-blue-green-black-cyan-orange-yellow-apple"))
