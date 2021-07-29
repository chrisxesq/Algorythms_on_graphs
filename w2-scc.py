import sys

sys.setrecursionlimit(200000)

def dfs(adj, visited, stack, i):
    visited[i]=True
    for k in adj[i]:
        if visited[k]==False:
            dfs(adj, visited, stack, k)
    stack.append(i)

def topo(adj):
    visited=[ False for _ in (adj)]
    stack = []
    for i in range(len(adj)):
        if visited[i] == False:
            dfs(adj, visited, stack, i)
    return stack[::-1]
    
def util(transpose_adj, visited, v):
        stack=[]
        if visited[v] == False:
            dfs(transpose_adj, visited, stack, v)
        return stack
    
def processing(transpose_adj, processing_stack):
    #print('pros',transpose_adj, processing_stack)
    visited=[ False for _ in (transpose_adj)]
    total=0
    for v in (processing_stack):
        #print('v,pros_stack',v)
        #print(processing_stack)
        #print(visited)
        stac=util(transpose_adj, visited, v)
        #print('stac',stac)
        if len(stac)>0:
            total += 1
    return total

if __name__ == '__main__':
    #data=[4,4,1,2,4,1,2,3,3,1]
    #data=[5,7, 2, 1, 3, 2, 3, 1, 4, 3, 4, 1, 5, 2, 5,3]
    #data=[10, 20, 7, 8, 4, 10, 3, 2, 1, 3, 4, 9, 2, 6, 8, 3, 8, 2, 6, 1, 6, 10, 10, 6, 1, 4, 3, 8, 1, 5, 8, 9, 5, 3, 3, 4, 5, 1, 8, 5, 8, 4]
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #print(edges)
    transpose_edges=list(zip(data[1:(2 * m):2],data[0:(2 * m):2]))
    #print(transpose_edges)
    transpose_adj = [[] for _ in range(n)]
    for (a, b) in transpose_edges:
        transpose_adj[a - 1].append(b - 1)
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #print('adj',adj)
    #print('transpose_adj',transpose_adj)
    processing_stack=(topo(adj))
    #print('processing_stack',processing_stack)
    print(processing(transpose_adj, processing_stack))