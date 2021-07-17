#Uses python3
#test

import sys

def reach(adj, x, y):
  connected=[]
  def util(adj, x, y):
      for n in range(len(adj)):
          if adj[n][0]==x:
              next = adj[n][1]
              connected.append(next)
              #print(adj[n])
              adj2 = adj[:]
              adj2[n]='v'
              if next == y:
                ans = 1
                return ans
              util(adj2, next, y)
        
      return 0
  util(adj, x, y)
  if y in connected:
    return 1
  else:
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #print('data',data)
    n, m = data[0:2]
    #print('n,m', n, m)
    data = data[2:]
    edges = list(zip[data[0:(2 * m):2], data[1:(2 * m):2]])
    #print('data,edges', data, edges)
    x, y = data[2 * m:]
    #print('x,y',x,y)
    adj = [[] for _ in range(n)]
    #print('adj',adj)
    x, y = x - 1, y - 1
    #print('x,y',x,y)
    for (a, b) in edges:
        print('a,b',a,b)
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
        # print('adj',adj)
    
    print(reach(adj, x, y))
    
# # Input:
# 4 3
# 1 2
# 3 2
# 4 3
# 1 4
 
# Your output:
# data [4, 3, 1, 2, 3, 2, 4, 3, 1, 4]
# n,m 4 3
# data,edges [1, 2, 3, 2, 4, 3, 1, 4] [(1, 2), (3, 2), (4, 3)]
# x,y 1 4
# adj [[], [], [], []]
# x,y 0 3
# a,b 1 2
# adj [[1], [0], [], []]
# a,b 3 2
# adj [[1], [0, 2], [1], []]
# a,b 4 3
#  adj [[1], [0, 2], [1, 3], [2]]

# # Correct output:
# # 1
