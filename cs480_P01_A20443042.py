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
    
def sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j][1] > arr[j+1][1]:
                #print(arr[j][1],arr[j+1][1])
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1] = temp
    return arr


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
        stateToNum[reader[i][0]] = i-1
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
    visited[actual_Src] = True
    cost = 0
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
        cost = cost + int(smf[3])
        if u == target:
            break
        count = 0
        for v, c in graphs[u]:
            if visited[v] == False:
                visited[v] = True
                count = count - 1
                pq.insert((slGraph[v][target][1], v,numToState[v],costList[u][v]))
        if(count==0):
            order.pop(len(order)-1)
        
    #print(visited[32])
    print(order)
    print(cost)
    #print(pq)
    #print(sort(order))
    


 
 
# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
#addedge(0, 1, 210)

src = stateToNum[sys.argv[1]]
dest = stateToNum[sys.argv[2]]

# src = stateToNum["MA"]
# dest = stateToNum["MD"]

best_first_search(src, dest, v)
# print("MD->WA:")
# best_first_search(stateToNum["MD"], stateToNum["WA"], v)
# print("MI->NM:")
# best_first_search(stateToNum["MI"], stateToNum["NM"], v)
# print("NH->AL:")
# best_first_search(stateToNum["NH"], stateToNum["AL"], v)
# print("OR->NY:")
# best_first_search(stateToNum["OR"], stateToNum["NY"], v)
# print("MA->AK:")
# best_first_search(stateToNum["MA"], stateToNum["AK"], v)
