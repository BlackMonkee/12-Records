import pickle
def elec():
    f=open('elections.dat','wb')
    y='y'
    while y=='y':
        l=[]
        p=input('party ')
        c=input('namr ')
        v=int(input('votes  '))
        s=input('status  ')
        l=[p,c,v,s]
        pickle.dump(l,f)
        y=input('y or n')
    f.close()
def read():
    f=open('elections.dat','rb')
    try:
        while True:
            l=pickle.load(f)
            print(l)
    except:
        print('File closed')
    f.close()
def cand():
    c=0
    f=open('elections.dat','rb')
    f2=open('elected.dat','wb')
    try:
        while True:
            l=pickle.load(f)
            if l[3]=='won':
                pickle.dump(l,f2)
                c=1
    except EOFError:
        if c!=1:
            print('none')
    f.close()
    f2.close
def red2():
    f=open('elected.dat','rb')
    try:
        while True:
            l=pickle.load(f)
            print(l)
    except EOFError:
        print()
    f.close()
elec()
read()
cand()
red2()
