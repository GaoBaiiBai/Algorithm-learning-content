'''
图最短路径的遍历一定是从该点到图的距离
'''
# import heapq
# pqueue=[]
# heapq.heappush(pqueue,(1,"A"))
# heapq.heappush(pqueue,(7,"B"))
# heapq.heappush(pqueue,(3,"C"))
# heapq.heappush(pqueue,(6,"D"))
# heapq.heappush(pqueue,(2,"E"))
# print(pqueue)
graph={
    "A":{"B":5,"C":1},
    "B":{"A":5,"C":2,"D":1},
    "C":{"A":1,"B":2,"D":4,"E":8},
    "D":{"B":1,"C":4,"E":3,"F":6},
    "E":{"C":8,"D":3},
    "F":{"D":6}
}
list1=[]
list2 =[]
def DFS(graph,start):
    global list1
    global  list2
    list1.append(start)
    for i in graph[start].keys():
        if i =="F":
            list1.append("F")
            list2.append(list1[::])
            list1.pop()
        else:
            if i in list1:
                pass
            else:
                DFS(graph,i)
                list1.pop()
DFS(graph,"A")
index1=1
for i in list2:
    sum = 0
    for key,index in zip(i[0:len(i)-1],i[1:len(i)]):
        sum +=graph[key][index]
    if index1==1:
        temp = sum
        index1+=1
    else:
        if sum<=temp:
            final_list = i
            temp = sum
print(final_list)
print(temp)
import math
def init_distance(graph,s):
    distance={s:0}
    for vertex in graph:
        if vertex!=s:
            distance[vertex] = math.inf
    return distance
import heapq
def dijkstra(graph,s):
    pqueue=[]
    heapq.heappush(pqueue,(0,s))
    seen = set()
    parent={s:None}
    distance=init_distance(graph,s)
    while (len(pqueue)>0):
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex =pair[1]
        seen.add(vertex)
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not  in seen:
                if dist+graph[vertex][w]<distance[w]:
                    heapq.heappush(pqueue,(dist+graph[vertex][w],w))
                    parent[w]=vertex
                    distance[w]=dist+graph[vertex][w]
    return parent,distance
parent,distance = dijkstra(graph,"A")
print(parent)
print(distance)