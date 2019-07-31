n=int(input())
T={}
n=7
root=list(range(1,n+1))
for i in range (1,n+1):  
    line=input().split()
    n_line=list(map(int,line))[1:]
    T[i]=n_line
    for k in n_line:
        root.remove(k)

def h(v):
    c_nodeo=T[v]  
    if c_nodeo ==[]:
        return 0
    else:
        return max(map(h,T[v]))+1
print(root[0])
print(sum(map(h,range(1,n+1))))



