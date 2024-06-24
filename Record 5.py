def wrdcnt():
    f=open('lines.txt','r')
    st=f.readlines()
    for i in st:
        s=(i.strip()).split(' ')
        if len(s)>=10:
            print(' '.join(s))
wrdcnt()
