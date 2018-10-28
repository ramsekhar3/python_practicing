def dfs(x,y,mat,n,m,visited):
    if ((x==n-1) and (y==m-1)):
        return True
    if ((x>n-1) or (y>m-1) or (x<0) or (y<0) ):
        return False
    if visited[x][y]==True:
        return False
    visited[x][y]=True
    if mat[x][y]==0:
        return False
    if ((dfs(x+1,y,mat,n,m,visited)) ==True):
        return True
    if ((dfs(x-1,y,mat,n,m,visited)) ==True):
        return True
    if ((dfs(x,y+1,mat,n,m,visited)) ==True):
        return True
    if ((dfs(x,y-1,mat,n,m,visited)) ==True):
        return True
    return False    

if __name__=='__main__':
    [n,m]=list(map(int,input().split()))
    mat=list()
    for i in range(n):
        mat.append(list(map(int,input().split())))
    visited=[[False]*n for _ in range(m)]        
    print ('Yes' if dfs(0,0,mat,n,m,visited)==True else 'No')
