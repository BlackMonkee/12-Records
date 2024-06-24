def arev():
    f=open('sample.txt','r')
    st=f.readlines()
    for i in st:
        s=i
        s=(s.strip()).split(' ')
        s=list(s)
        for j in range(len(s)):
            if s[j][0]=='o':
                k=s[j][-1::-1]
                s[j]=k
        print(' '.join(s))
arev()
