'''
Please find the below code for minimum spanning Tree
'''
import os
from collections import defaultdict
class Graph():
    def __init__(self,vertices):
        self.V=vertices
        self.graph=list()
    def Node(self):
        self.parent=list()
        self.rank=list()
        for i in range(self.V+1):
            self.parent.append(i)
            self.rank.append(0)
    def findp(self,x):
        if self.parent[x] == x:
            return x
        return self.findp(self.parent[x])
    def union(self,x,y):
        xp=self.findp(x)
        yp=self.findp(y)
        if self.rank[xp]>self.rank[yp]:
           self.parent[yp]=self.parent[xp]
        elif self.rank[xp]<self.rank[yp]:
           self.parent[xp]=self.parent[yp]
        else:
            self.parent[yp]=self.parent[xp]
            self.rank[xp]+=1
    def mst(self):
        self.Node()
        self.graph=sorted(self.graph,key=lambda item:item[2])
        self.result =list()
        e=0
        i=0
        while e<self.V -1:
            u,v,w=self.graph[i]
            up=self.findp(u)
            vp=self.findp(v)
            i+=1
            if up!=vp:
                self.result.append([u,v,w])
                self.union(up,vp)
                e+=1
                
 
if  __name__=="__main__":
    l=input().split()
    N=int(l[0])
    M=int(l[1])
    g=Graph(N)
    for i in range(M):
        l=list(map(int,input().split()))
        #k=map(,l)
        g.graph.append(l)
    #print (g.graph)
    g.mst()
    s=0
    for i in g.result:
        s+=i[2]
    print (s)    
