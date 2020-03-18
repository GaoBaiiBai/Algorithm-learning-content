graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","C","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}
# import queue
# a = queue.Queue()
# a.put(1)
# print(a.qsize())
# print(a.empty())
# print(a.get())
def BFS(graph,start):
    queue=[]
    queue.append(start)
    seen =[]
    seen.append(start)
    while(len(queue)>0):
        vertex = queue.pop(0)
        node = graph[vertex]
        for w in node:
            if w not in seen:
                queue.append(w)
                seen.append(w)
        print(vertex)
BFS(graph,"A")
print('----------')
def DFS(graph,start):
    stack=[]
    stack.append(start)
    seen =[]
    seen.append(start)
    while(len(stack)>0):
        vertex = stack.pop()
        node = graph[vertex]
        for w in node:
            if w not in seen:
                stack.append(w)
                seen.append(w)
        print(vertex)
DFS(graph,"A")
print('----------')
def BFS(graph,s):
    queue=[]
    queue.append(s)
    seen = set()
    seen.add(s)
    parent={s:None}
    while (len(queue)>0):
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not  in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent
p = BFS(graph,"E")
print("---------")
""" B->E"""
print("A")
key = p["A"]
print(key)
while p[key]!=None:
    key = p[key]
    print(key)
