a=[]
s=[]
l=[]
u=[]
with open('matrix.txt', 'r') as file:
        r,c = map(int, file.readline().split())
        a=[]
        for i in range(r):
            row = list(map(float, file.readline().split()))
            a.append(row)
        for i in range(len(a)):
            a[i].append(0)
print("Rows:", r)
print("Columns:", c)
print("Augmented Matrix [A 0]:", a) 

u=a
#converting to ref.
for i in range(len(u)):
    nonzero=i
    for j in range(i+1,len(u)):
        if abs(u[j][i])>abs(u[nonzero][i]):
            nonzero=j
    u[i],u[nonzero]=u[nonzero],u[i]
    for j in range(i+1,len(u)):
        if u[i][i]==0:
            d=u[j][i]/1
        else:
            d=u[j][i]/u[i][i]
        for k in range(i,len(u[0])):
            u[j][k]-=(d*u[i][k])

#checking if matrix has nontrivial solutions or not.
f=0
for i in u:
    f=0
    for j in i:
        if j==0:
            f+=1
        elif j!=0:
            break
if f==c:
    print('trivial solution for matrix,x1=0,x2=0,x3=0')
else:
    print('non-trivial solns for matrix.')
u=u[::-1]
#rounding
for i in range(len(u)):
    for j in range(len(u[i])):
        if 'e' in str(u[i][j]):
            u[i][j]=0
#converting to rref.
p=[]
for i in range(len(u)):
    c=0
    p=[]
    for k in u[i]:
        if k!=0 and c==0:
            for t in range(len(u[i])):
                p.append((u[i][t]/k+0))
                c+=1
            u[i]=p
for i in range(len(u)):
    for j in u[i+1:]:
        c=0
        for k in u[i]:
            if k==0:
                pass
            elif c==0 and k!=0:
                c+=1
                d=u[i].index(k)
                o=j[d]
                for t in range(len(j)):
                    j[t]-=(u[i][t]*o+0)
u=u[::-1]
#rounding
for i in range(len(u)):
    for j in range(len(u[i])):
        if 'e' in str(u[i][j]):
            u[i][j]=0
for i in u:
    for j in i:
        if len(str(j))>3:
            k=str(j)[:6]
            i[i.index(j)]=eval(k)

#placing all 0s row at last.
def fnc2(t):
    c=0
    d=0
    g=[]
    for i in t:
        flag=True
        for j in i:
            if j!=0:
                flag=False
        if flag==True:
            c+=1
    for j in range(len(t)-c):
        copy=t.copy()
        for i in copy:
            if i[d]!=0:
                g.append(i)
                t.remove(i)
        d+=1
    g+=t
    return g
b=fnc2(u[::-1])
u=b
for i in u:
    for j in i:
        print(j,end=' ')
    print()

#finding free variables, fixed variables, index of free variables, index of pivots.
v = []
fixvar=[]
freeindex=[]
for i in range(len(u)):
    c = 0
    for j in range(len(u[i])-1):
        if u[i][j] == 1 and c == 0:
            v.append('x' + str((j) + 1))
            fixvar.append('x' + str((j) + 1))
            c += 1
for j in range(len(u[0])-1):
    if ('x' + str(j + 1)) not in v:
        v.insert(j,0)
o=[]
for i in v:
    if i!=0:
        o.append(v.index(i))
for j in range(len(u[0])-1):
    for k in range(len(v)):
        if v[k]==0:
            v.remove(0)
            v.insert(k,'x' + str(k + 1))
for i in o:
    for j in range(len(v)):
        if j==i:
            v.remove('x' + str(j + 1))
            v.insert(j,0)
c=0
for i in v:
    if i==0:
        c+=1
for i in range(c):
    v.remove(0)
print('Free variables are:',v)
print('Fixed variables are:',fixvar)
pivot=[]
for i in range(len(u)):
    for j in range(len(u[0])):
        if u[i][j]!=0:
            pivot.append(j)
            break
for i in range(len(u[0])-1):
    if i not in pivot:
        freeindex.append(i)
for i in range(len(u)):
    c=0
    a=''
    for j in range(len(u[i])):
        if u[i][j]!=0 and c==0:
            a+='x' + str((j) + 1)+'='
            c+=1
        else:
            if u[i][j]!=0:
                a+=str(-u[i][j])+'*'+'x' +str((j) + 1)+'+'
    print(a[:-1]) 

#Finding gen soln and printing it in parametric form.
ans=[]
i=0
while i<len(u[0])-1:
    i+=1
    if i not in pivot:
        ans.append([0]*(len(u[0])-1))
a=0
b=0
j=0
while j<(len(u[0])-1):
    if j not in pivot:
        ans[a][j]+=1
        a+=1  
    else: 
        x=0
        for k in freeindex:
            ans[x][j]-=u[b][k]
            x+=1
        b+=1  
    j+=1
s=''
for i in range(len(v)):
    s+=str(v[i])+'*'+str(ans[i])+'+'
print(s[:-1])