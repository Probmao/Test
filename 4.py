m = 0
for x in range(2031):
    a = 7**150-7**100-x
    k = 0
    while a>0:
        if a%5==0:
            k+=1
        a = a//5
    if k>m:
        m = k
        print(m,x)

    
