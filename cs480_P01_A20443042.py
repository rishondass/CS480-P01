#!/usr/bin/python
import csv, sys
from pprint import pprint
from PQ import PriorityQueue
#from queue import PriorityQueue
from AdjacencyList import Graph










graph = {}
stateToNum = {}
numToState = {}

def addedge(g,x, y, cost):
    g[x].append((y, cost))


with open('driving.csv', newline='') as csvfile:
    reader = list(csv.reader(csvfile))
    v = len(reader)-1
    graphs = [[] for i in range(v)]
    alGraph = Graph(v)
    costList = [[0 for x in range(v)] for y in range(v)]
    for i in range(0, len(reader)-1):
        temp = []
        for j in range(0,len(reader[i])-1):
            cost = reader[i+1][j+1]
            if (int(cost) > 0):
                addedge(graphs,i,j,cost)
                alGraph.add_edge(i,j,cost)
                temp.append({"state":reader[0][j+1], "weight": reader[i+1][j+1]})
                graph[i]= {"state":reader[i][0], "data":temp}
            costList[i][j]=cost
        stateToNum[reader[i+1][0]] = i
        numToState[i] = reader[i+1][0]
        

    #print(graphs[17])
    #print(numToState)
    #print(stateToNum)
    #print(someList[0][8])
  
    
    

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

def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    order = []
    pq.insert((0, actual_Src,numToState[actual_Src],costList[actual_Src][actual_Src]))
    visited[actual_Src] = numToState[actual_Src]
    while pq.isEmpty() == False:
        #print(pq)
        smf = pq.delete()
        #print(str(smf))
        u = smf[1]
        
        # Displaying the path having lowest cost
        #print(numToState[u], end=" ")
        order.append(numToState[u])
        # cost = cost+smf[2]
        #print(cost)
        if u == target:
            break
        
        for v, c in graphs[u]:
            if visited[v] == False:
                visited[v] = numToState[u]
                pq.insert((slGraph[v][target][1], v,numToState[v],costList[u][v]))
        
            
        
    #print(visited[32])
    #print(order)
    order.reverse()
    #print(order)
    #print(visited)
    path = []
    #print(numToState[visited[stateToNum[order[0]]]])
    #print(numToState[visited[stateToNum[order[1]]]])
    
    curr = visited[target]
    for x in order:
        path.append(curr)
        if(stateToNum[curr] == actual_Src):
            break
        curr = visited[stateToNum[path[len(path)-1]]]
       
    path.reverse()
    
    path.append(numToState[target])
    #print(cost)
    #print(pq)
    #print(sort(order))
    print(path)
    
    
    cost = 0
    for i in range(1,len(path)):
        if (i!=0):
            cost = cost + int(costList[stateToNum[path[i-1]]][stateToNum[path[i]]])
    print(cost)
    

def A(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    order = []
    pq.insert((0, actual_Src))
    visited[actual_Src] = (numToState[actual_Src],0)
    
    while pq.isEmpty() == False:
        #print(pq)
        smf = pq.delete()
        #print(str(smf))
        u = smf[1]
        
        # Displaying the path having lowest cost
        #print(numToState[u], end=" ")
        order.append(numToState[u])
        # cost = cost+smf[2]
        #print(cost)
        if u == target:
            break
        prevCost = int(visited[u][1])
        for v, c in graphs[u]:
            if visited[v] == False:
                visited[v] = (numToState[u],int(costList[u][v])+prevCost)
                totalVal = int(slGraph[v][target][1])+(int(costList[u][v])+visited[u][1])
                #totalVal = (int(costList[u][v])+visited[u][1])
                pq.insert((totalVal, v,numToState[v],costList[u][v],slGraph[v][target][1]))
                if v == target:
                    break
        
            
        
    #print(visited[32])
    # print("Order:==================")
    # print(order)
    # order.reverse()
    # print(order)
    # print("==================\n\n")
    # print("Visited:==================")
    # print(visited)
    # print("==================\n\n")
    path = []
    #print(numToState[visited[stateToNum[order[0]]]])
    #print(numToState[visited[stateToNum[order[1]]]])
    curr = visited[target][0]
    for x in order:
        path.append(curr)
        if(stateToNum[curr] == actual_Src):
            break
        curr = visited[stateToNum[path[len(path)-1]]][0]
        
       
    path.reverse()
    path.append(numToState[target])
    #print(cost)
    #print(pq)
    #print(sort(order))
    print(path)
    
    
    cost = 0
    for i in range(1,len(path)):
        if (i!=0):
            cost = cost + int(costList[stateToNum[path[i-1]]][stateToNum[path[i]]])
    print(cost)

# src = stateToNum[sys.argv[1]]
# dest = stateToNum[sys.argv[2]]

# src = stateToNum["MA"]
# dest = stateToNum["MD"]

#best_first_search(src, dest, v)
#A(src,dest,v)
# print("MA->MD:")
# best_first_search(stateToNum["MA"], stateToNum["MD"], v)
# A(stateToNum["MA"], stateToNum["MD"], v)
# print("MD->WA:")
# best_first_search(stateToNum["MD"], stateToNum["WA"], v)
# A(stateToNum["MD"], stateToNum["WA"], v)
# print("MI->NM:")
# best_first_search(stateToNum["MI"], stateToNum["NM"], v)
# A(stateToNum["MI"], stateToNum["NM"], v)
print("NH->AL:")
best_first_search(stateToNum["NH"], stateToNum["AL"], v)
A(stateToNum["NH"], stateToNum["AL"], v)
print("OR->NY:")
best_first_search(stateToNum["OR"], stateToNum["NY"], v)
A(stateToNum["OR"], stateToNum["NY"], v)
# print("MA->AK:")
# best_first_search(stateToNum["MA"], stateToNum["AK"], v)
# A(stateToNum["MA"], stateToNum["AK"], v)
