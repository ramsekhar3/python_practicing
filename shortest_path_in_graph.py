import os
import sys
import heapq
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
    s=[]
    heapq.heappush(s,(0,1))
    while len(s)>0:
        temp=heapq.heappop(s)
        x=temp[1]
        if visited[x]==True:
            continue
        for i in g[x]:
            visited[x]=True
            if visited[i]==False:
                if d[x]+D[x][i]<d[i]:
                    d[i]=d[x]+D[x][i]
                    heapq.heappush(s, (d[i],i))
    print (d)
    #for key,value in d.items():
    #    if key==1:
    #        continue
    #    print (d[key],end=' ')
        
if __name__ =='__main__':
    l=input().split()
    [n,m]=list(map(int,l))
    g=defaultdict(list)
    D=defaultdict(dict)
    #print (n,m)
    ew=list()
    for i in range(m):
        l=input().split()
        l=list(map(int,l))
        D[l[0]][l[1]]=l[2]
        D[l[1]][l[0]]=l[2]
        ew.append(l)
        g[l[0]].append(l[1])
        g[l[1]].append(l[0])
    djks(g,D)    
