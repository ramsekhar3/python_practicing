import os
import sys
from collections import defaultdict

def aputil(g,disc,low,parent,visited,time,ap,v,bridge):
    visited[v]=True
    low[v]=disc[v]=time+1
    child=0
    for i in g[v]:
        #print (i,v,visited)
        if visited[i]==False:
            child=child+1
            parent[i]=v
            aputil(g,disc,low,parent,visited,(time+1),ap,i,bridge)
            low[v]=min(low[v],low[i])
            #print (v,i,low[v],low[i],disc[i],disc[v])
            if parent[v]==-1 and child>1:
                ap[v]=True
            if parent[v]!=-1 and low[i]>=disc[v]:
                ap[v]=True
            if low[i]>disc[v]:
                bridge[v].append(i)
        elif i!=parent[v]:
            low[v]=min(low[v],disc[i])
                
if __name__=='__main__':
    [n,m]=list(map(int,input().split()))
    g=defaultdict(list)
    for _ in range(m):
        k=list(map(int,input().split()))
        g[k[0]].append(k[1])
        g[k[1]].append(k[0])
    visited=[False]*(n)
    ap=[False]*(n)
    disc=[sys.maxsize]*(n)
    low=[0]*(n)
    time=0
    parent=[-1]*(n)
    vertex=0
    bridge=defaultdict(list)
    aputil(g,disc,low,parent,visited,time,ap,vertex,bridge)
    c=ap.count(True)
    print (c)
    for index,value in enumerate(ap):
        if value==True:
            print (index)
    c=0
    for key,value in bridge.items():
        c+=len(value)
    print (c)
    for key,value in bridge.items():
        for i in value.:
            print(key,i)
