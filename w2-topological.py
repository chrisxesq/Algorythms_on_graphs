#Uses python3

import sys

def dfs(adj, visited, stack, i):
    visited[i]=True
    for k in adj[i]:
        if visited[k]==False:
            dfs(adj, visited, stack, k)
    stack.append(i)


def toposort(adj):
    visited=[ False for _ in (adj)]
    stack = []
    for i in range(len(adj)):
        if visited[i] == False:
            dfs(adj, visited, stack, i)
    return (stack[::-1])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    stack=toposort(adj)
    for i in stack:
        print(i+1, end=' ')
