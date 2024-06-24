def endy():
    f=open('bookname.txt','r')
    st=f.readlines()
    c=0
    for i in st:
        s=i.strip()
        if s[-1]=='y':
            print(i,end='')
            c+=1
    print(c)
endy()
