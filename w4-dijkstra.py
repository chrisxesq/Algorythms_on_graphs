import sys
def min(data):
  m=float('inf')
  val=''
  for i in range(len(data)):
    if data[i]<m:
      m=data[i]
      val=i
  return i

def distance(adj, cost, s, t):
    id=[_ for _ in range(len(adj))]
    dist=[ float('inf') for _ in adj]
    prev=[None for _ in adj]
    dist[s]=0
    q=[]
    q.append(dist[s])
    while len(q)>0:
      min_i=min(q)
      cur_processing = q[min_i]
      q.remove(q[min_i])
      for i in range(len(adj[cur_processing])):
        exploring_index = adj[cur_processing][i]
        cost_index=adj[cur_processing].index(exploring_index)
        if dist[exploring_index]>dist[cur_processing]+cost[cur_processing][cost_index]:
          dist[exploring_index]=dist[cur_processing]+cost[cur_processing][cost_index]
          prev[exploring_index]=cur_processing
          q.append(exploring_index)
    if dist[t]!= float('inf'):
        return dist[t]

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data=[4,4,1,2,1,4,1,2,2,3,2,1,3,5,1,3]
    #data=[5,9,1,2,4,1,3,2,2,3,2,3,2,1,2,4,2,3,5,4,5,4,1,2,5,3,3,4,4,1,5]
    #data=[3,3,1,2,7,1,3,5,2,3,2,3,2]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))