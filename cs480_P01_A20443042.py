#!/usr/bin/python
import csv, sys
from pprint import pprint
from PQ import PriorityQueue
#from queue import PriorityQueue










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
                print(arr[j][1],arr[j+1][1])
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1] = temp
    return arr


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

    #print(graphs[17])
    #print(numToState)
    #print(stateToNum)
    #print(someList[17])
  
    
    

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
    pq.insert((0, actual_Src))
    visited[actual_Src] = True
    while pq.isEmpty() == False:
        print(pq)
        smf = pq.delete()
        #print(str(smf))
        u = smf[1]
        
        # Displaying the path having lowest cost
        #print(numToState[u], end=" ")
        order.append(numToState[u])
        if u == target:
            break
        temp = -1
        for v, c in graphs[u]:
            if visited[v] == False:
                visited[v] = True
                pq.insert((slGraph[v][target][1], v,numToState[v]))
    print(order)
    #print(sort(order))

 
 
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