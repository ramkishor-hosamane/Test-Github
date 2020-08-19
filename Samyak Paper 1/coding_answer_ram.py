def find_path(mat,row,col,m,n):
    if row >= m or col >=n:
        return 0
    if row==m-1 and col == n-1:
        return 1
    
    return find_path(mat,row+1,col,m,n)+find_path(mat,row,col+1,m,n)
def solve(m,n):
    mat = [[0 for i in range(n)] for j in range(m)]
    return find_path(mat,0,0,m,n)
    


T = int(input())
for _ in range(T):
    M,N = list(map(int,input().split()))
    print(solve(M,N))
    