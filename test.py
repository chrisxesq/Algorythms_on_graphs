import sys
import heapq

def distance(adj, cost, s, t):

    longest = []
    for item in cost:
        longest.extend(item)

    inf=sum(longest)+1
    dist = [inf for i in adj]
    #prev = [-1  for i in adj]

    dist[s] = 0

    def ChangePriority(H, v):
        insert=[dist[v],v]
        heapq.heappush(H,insert)
        #print(H)
        return H 

    H = [[dist[s],s]]
    heapq.heapify(H)

    while H:
        #print(H)
        _u=heapq.heappop(H)
        u=_u[1]
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                H = ChangePriority(H, v)

    if dist[t] == inf:
        return -1
    return dist[t]


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