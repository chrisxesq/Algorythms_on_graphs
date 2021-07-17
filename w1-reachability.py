#Uses python3
#test

import sys

def reach(adj, x, y):
  connected=[]
  def util(adj, x, y):
      if len(adj[x])==0:
        return connected
      else:
        for i in range(len(adj[x])):
          new = adj[x][i]
          if new == 'visited':
              return connected
          if new not in connected:
            connected.append(adj[x][i])
          adj[x][i]='visited'
          if new==y:
            return connected
          else:
            util(adj, new, y)
        return connected
  list = util(adj,x,y)
  if x in list and y in list:
      return 1
  else:
      return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
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
