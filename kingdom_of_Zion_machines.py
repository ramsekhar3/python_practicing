import math
import os
import random
import re
import sys
import heapq
from collections import defaultdict

# Complete the minTime function below.
def minTime(roads, machines,nodes):
    n =len(roads)
    m=len(machines)
    g=defaultdict(list)
    roads_vis=[[False]*nodes for _ in range(nodes)]
    for i in range(n):
        g[roads[i][0]].append((roads[i][1],roads[i][2]))
        g[roads[i][1]].append((roads[i][0],roads[i][2]))
        #print(i,roads[i][0],roads[i][1])
        roads_vis[roads[i][0]][roads[i][1]]=True
        roads_vis[roads[i][1]][roads[i][0]]=True
    #print (g,roads_vis)
    roads_del=[]
    result=0
    for temp in machines:
        visited=[False]*(nodes)
        s=[]
        heapq.heappush(s,temp)
        roads_to_be_removed=list()
        while len(s)>0:
            x=heapq.heappop(s)
            visited[x]=True
            for t in g[x]:
                k=t[0]
                d=t[1]
                if visited[k]==False and roads_vis[x][k] ==True:
                    visited[k]==True
                    heapq.heappush(s,k)
                    roads_to_be_removed.append([x,k,d])
                    if k in machines:
                        roads_to_be_removed=sorted(roads_to_be_removed,key=lambda item:item[2])
                        r=roads_to_be_removed.pop(0)
                        roads_vis[r[1]][r[0]]=False
                        roads_vis[r[0]][r[1]]=False
                        print (k,r)
                        result=result+r[2]
    return result    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []

    for _ in range(n - 1):
        roads.append(list(map(int, input().rstrip().split())))

    machines = []

    for _ in range(k):
        machines_item = int(input())
        machines.append(machines_item)

    result = minTime(roads, machines,n)

    fptr.write(str(result) + '\n')

    fptr.close()
