#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from collections import defaultdict

# Complete the minTime function below.
def minTime(roads, machines):
    n =len(roads)+1
    m=len(machines)
    g=defaultdict(list)
    roads_to_be_removed=defaultdict(list)
    roads_vis=[[False]*n for _ in range(n)]
    for i in range(n):
        g[roads[i][0]].append((roads[i][1],roads[i][2]))
        g[roads[i][1]].append((roads[i][0],roads[i][2]))
        roads_vis[roads[i][0]][roads[i][1]]=True
        roads_vis[roads[i][1]][roads[i][0]]=True
    visited=[False]*(n)
    s=[]
    for temp in machines:
        heapq.heappush(s,temp)
        while len(s)>0:
            x=heapq.heappop(s)
            visited[x]=True
            for t in g[x]:
                k=t[0]
                d=t[1]
                if visited[k]==False:
                    visited[k]==True
                    heapq.heappush(k)
                    roads_to_be_removed.append([x,k,d])
                    if k in machines:
                        road_del=sorted(roads_to_be_removed,key=lambda item:item[2])
                        roads_vis[roads_del[0][1]][roads_del[0][0]]=False
                        roads_vis[roads_del[0][0]][roads_del[0][1]]=False
                        result=result+roads_del[0][2]
    
        
    

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

    result = minTime(roads, machines)

    fptr.write(str(result) + '\n')

    fptr.close()
