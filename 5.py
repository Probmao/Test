def p(x):
    return x>1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))

def div(x):
    d = set()
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
k = []

for x in range(158928,345293+1):
    q = [i for i in div(x) if p(i)]
    if len(q)==3 and q[0]*q[1]*q[2]==x:
        k.append(x)
print(k[0],len(k))
