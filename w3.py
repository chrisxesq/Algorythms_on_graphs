import sys
from collections import deque 

def distance(adj, s, t):
    dist=[ 'inf' for _ in (adj)]
    #print('dist',dist)
    q=deque([s])
    dist[s]=0
    #print(dist)
    while len(q)!=0:
      u=q.popleft()
      #print(u)
      #print(q)
      for i in adj[u]:
        if dist[i]=='inf':
          q.append(i)
          dist[i]=dist[u]+1
    if dist[t] == 'inf':
        return -1
    return dist[t]

if __name__ == '__main__':
    #data=[4,4,1,2,4,1,2,3,3,1,2,4]
    #data=[5,4,5,2,1,3,3,4,1,4,3,5]
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    #print(edges)
    #print(adj)
    #print(s,t)
    print(distance(adj, s, t))
