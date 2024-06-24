def dic(d):
    l=[]
    for i in d:
        if d[i] not in l:
            print(d[i])
            l+=d[i],
dic({'a':1,'b':3,'c':4,'d':6,'f':3,'e':6})
