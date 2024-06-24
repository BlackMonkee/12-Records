def enda():
    f=open('lines.txt','r')
    st=f.readlines()
    c=0
    for i in st:
        s=(i.strip()).split(' ')
        s=list(s)
        for j in range(len(s)):
            if s[j][-1].isdigit():
                print(s[j])
                c+=1
    print(c," words end with a digit")
enda()
 
