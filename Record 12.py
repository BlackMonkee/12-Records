import pickle
def stud():
    f=open('12science.dat','wb')
    y='y'
    while y=='y':
        d={}
        s=input('section- ')
        t=int(input('total- '))
        su=input('sub- ')
        d[s]=[t,su]
        pickle.dump(d,f)
        y=input('y or n')
    f.close()
def read():
    f=open('12science.dat','rb')
    try:
        while True:
            l=pickle.load(f)
            print(l)
    except EOFError:
        print('File closed')
    f.close()
def modify():
    f=open('12science.dat','rb+')
    s=input('sub- ')
    h=0
    try:
        while True:
            p=f.tell()
            d=pickle.load(f)    
            for i in d:
                if d[i][1]==s:
                    h=1
                    t=d[i][0]+1
                    d[i][0]=t
                    f.seek(p)
                    pickle.dump(d,f)
    except EOFError:
        if h==0:
            print('NO  PRESENT')
    f.close()
def read2():
    f=open('12science.dat','rb')
    try:
        while True:
            l=pickle.load(f)
            print(l)
    except:
        print('File closed')
    f.close()
#stud()
read()
modify()
read2()
