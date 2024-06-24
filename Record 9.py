import pickle
def IPL():
    f=open('ipl.dat','wb')
    y='y'
    while y=='y':
        d={}
        t=input('Team name- ')
        m=int(input('Matches played- '))
        w=int(input('Ws- '))
        l=int(input('Ls- '))
        d[t]=[m,w,l]
        pickle.dump(d,f)
        y=input('y or n')
    f.close()
def quali():
    c=0
    f=open('ipl.dat','rb')
    try:
        while True:
            d=pickle.load(f)
            for i in d:
                if d[i][1]>6:
                    print(d)
                    c=1
    except EOFError:
        if c!=1:
            print('absent')
    f.close()
#IPL()
quali()
