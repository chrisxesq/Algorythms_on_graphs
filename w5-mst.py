#Uses python3
#kruskal: repeatedly add the next lightest edge if this doesnt produce a cycle

import math
import sys

def dist(x,y):
    [x1,y1]=x
    [x2,y2]=y
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def util(n,x,y):
    edges=[]
    for i in range(n):
      for j in range(n):
        if i!=j and i < j:
          v=((i,j),dist([x[i],y[i]],[x[j],y[j]]))
          edges.append(v)
    return edges

def util2(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[i].isdisjoint(a[j])==False:
                a[i]=a[i].union(a[j])
                a[j]=a[i]
    for i in range(len(a)):
        for j in range(len(a)-1):
            if i!=j and a[i]==a[j]:
                a[j]={}
    k=[]
    for i in range(len(a)):
        if len(a[i])!=0:
            k.append(a[i])
    return k

def minimum_distance(n, edges):
    
    cost=0
    path=[set()]
    
    
    sorted_edges=sorted(edges, key=lambda x:x[1])
    for edge in range(len(sorted_edges)):
      e1=sorted_edges[edge][0][0]
      e2=sorted_edges[edge][0][1]
      c=sorted_edges[edge][1]
      #print('e1,e2,c',e1,e2,c)
      ctr=0
      for i in range(len(path)):


          if len({e1,e2}&path[i])==0:
            ctr+=1 
            if ctr==len(path):
              path.append({e1,e2})
              cost += c
              
          elif len({e1,e2}&path[i])==1:
            path[i].add(e1)
            path[i].add(e2)
            cost += c

            path=util2(path)

            break
          elif len({e1,e2}&path[i])==2:
            break

    
    return cost


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data=[4,0,0,0,1,1,0,1,1]
    #data=[5,0,0,0,2,1,1,3,0,3,2]
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    edges= util(n,x,y)
    print("{0:.9f}".format(minimum_distance(n,edges)))
