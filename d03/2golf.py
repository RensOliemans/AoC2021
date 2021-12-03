def o(l, p, i):
    e=len
    if e(l)==1:
        return int(l[0],2)
    mc = int(e([n[p] for n in l if n[p]=='1'])/e(l)>=.5)
    if i:
        mc=1-mc
    l=[n for n in l if n[p]==str(mc)]
    return o(l,p+1,i)
p=list(open('3'))
print(o(p,0,1)*o(p,0,0))