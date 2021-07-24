listA =[]
def stack(adj):
    TFtable=[ 'f' for _ in (adj)]
    #print('table',TFtable)
    def util(i):
        #print(i,adj[i])
        if len(adj[i])==0:
            listA.append(i)
            #print('list',listA)
            return 0
        else:
            for j in range(len(adj[i])):
                #print('j',j)
                if TFtable[j] == 'f':
                    TFtable[j] = 't'
                    util(j)
                else:
                    if listA[-1] != i:
                        listA.append(i)
    for i in range(len(adj)):
        #print('main loop',i,adj[i])
        if TFtable[i] == 'f':
            TFtable[i]='t'
            util(i)        
    return 0

    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2*m):2], data[1:(2*m):2]))
    #print(edges)
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #print('adj',adj)
    stack(adj)
    ans=[]
    while len(listA)>0:
        ans.append(listA.pop()+1)
    for x in ans:
          print(x, end='')  



    
    