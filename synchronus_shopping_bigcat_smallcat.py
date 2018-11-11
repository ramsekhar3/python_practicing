import os
import sys
from collections import defaultdict
import heapq

if __name__=='__main__':
    N,M,K=list(map(int,input().split()))
    fish=[0]*(N+1)
    g=defaultdict(list)
    D=defaultdict(dict)
    needstate=((1<<K)-1)
    for i in range(1,N+1):
        temp=list(map(int,input().split()))
        for j in temp[1:]:
            fish[i]|=(1<<(j-1))
    for _ in range(M):
        temp=list(map(int,input().split()))
        D[temp[0]][temp[1]]=temp[2]
        D[temp[1]][temp[0]]=temp[2]
        g[temp[0]].append(temp[1])
        g[temp[1]].append(temp[0])
    visited=[[False]*(1<<K) for _ in range(N+1)]
    d=[[sys.maxsize]*(1<<K) for _ in range(N+1)]
    s=[]
    d[1][fish[1]]=0
    heapq.heappush(s,(0,1,fish[1]))
    while len(s)>0:
        c,n,st=heapq.heappop(s)
        visited[n][st]=True
        for k in g[n]:
            ns=st|fish[k]
            if visited[k][ns]==False:
                if d[n][st]+D[n][k]<d[k][ns]:
                    d[k][ns]=d[n][st]+D[n][k]
                    heapq.heappush(s,(d[k][ns],k,ns))
    ans=sys.maxsize
    #print(d)
    i=fish[1]
    while (i<(1<<(K))):
        j=fish[1]
        while(j<(1<<(K))):
            if(i|j==needstate):
                ans=min(ans,max(d[N][i],d[N][j]))
            j+=1   
        i+=1    
                
    print (ans) 
