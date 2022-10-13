#!/usr/bin/python
import csv, sys
import queue
from pprint import pprint
from queue import PriorityQueue










graph = {}
stateToNum = {}
numToState = {}

def addedge(g,x, y, cost):
    g[x].append((y, cost))


with open('driving.csv', newline='') as csvfile:
    reader = list(csv.reader(csvfile))
    v = len(reader)-1
    graphs = [[] for i in range(v)]
    someList = []
    for i in range(0, len(reader)-1):
        temp = []
        for j in range(0,len(reader[i])-1):
            cost = reader[i+1][j+1]
            if (int(cost) > 0):
                addedge(graphs,i,j,cost)
                temp.append({"state":reader[0][j+1], "weight": reader[i+1][j+1]})
                graph[i]= {"state":reader[i][0], "data":temp}
        stateToNum[reader[i][0]] = i-1
        numToState[i] = reader[i+1][0]
        someList.append(temp)

    print(graphs[17])
    #print(numToState)
    #print(stateToNum)
    print(someList[17])
  
    
    

with open('straightline.csv', newline='') as csvfile:
    reader1 = list(csv.reader(csvfile))
    v = len(reader1)-1
    slGraph = [[] for i in range(v)]
    for i in range(0, len(reader1)-1):
        for j in range(0,len(reader1[i])-1):
            cost = reader1[i+1][j+1]
            addedge(slGraph,i,j,cost)

#distance from CT->MD
# print(slGraph[5][18][1])
# print(slGraph[28][18])
# print(slGraph[32][18])
# print(slGraph[37][18])
# print(slGraph[44][18])













 
# Function For Implementing Best First Search
# Gives output path having lowest cost
order = []
def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    queue = []
    #pq.put((0, actual_Src))
    queue.append((0,actual_Src))
    visited[actual_Src] = True
    while queue != []:
        u = queue.pop(0)[1]
        
        # Displaying the path having lowest cost
        print(numToState[u], end=" ")
        order.append(u)
        if u == target:
            break
        temp = -1
        for v, c in graphs[u]:
            if visited[v] == False:
                visited[v] = True
                queue.append((slGraph[v][target][1], v))
    # while pq.empty() == False:
    #     u = pq.get()[1]
        
    #     # Displaying the path having lowest cost
    #     print(numToState[u], end=" ")
    #     order.append(u)
    #     if u == target:
    #         break
    #     temp = -1
    #     for v, c in graphs[u]:
    #         if visited[v] == False:
    #             visited[v] = True
    #             pq.put((slGraph[v][target][1], v))
    print(queue)
    print()
 

 
 
# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
#addedge(0, 1, 210)

# src = stateToNum[sys.argv[1]]
# dest = stateToNum[sys.argv[2]]

src = stateToNum["MA"]
dest = stateToNum["MD"]

best_first_search(src, dest, v)
# for i in order:
#     print(numToState[i])