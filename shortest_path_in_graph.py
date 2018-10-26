import os
import sys
from collections import defaultdict 
class Vertex():
    def __init__(self,node):
        self.adj={}
        self.id=node
        self.visited=False
        self.distance=sys.maxsize
        

def djks(g,D):
    d=dict()
    for i in range(1,n+1):
        d[i]=sys.maxsize
    d[1]=0 
    visited=[False]*(n+1)
    result=dict()
    s=list()
    s.append([1,0])
    while len(s)>0:
        temp=s.pop()
        x=temp[0]
        if visited[x]==True:
            continue
        for i in g[x]:
            visited[x]=True
            if visited[i]==False:
                if d[x]+D[x][i]<d[i]:
                    d[i]=d[x]+D[x][i]
                    s.append([i,d[i]])
                    result[x]=i
    print (result)    
if __name__ =='__main__':
    l=input().split()
    [n,m]=list(map(int,l))
    g=defaultdict(list)
    D=defaultdict(dict)
    #print (n,m)
    ew=list()
    for i in range(m):
        l=input().split()
        k=list(map(int,l))
        D[l[0]][l[1]]=l[2]
        D[l[1]][l[0]]=l[2]
        ew.append(k)
        g[l[0]].append(l[1])
        g[l[1]].append(l[0])
    djks(g,D)    
