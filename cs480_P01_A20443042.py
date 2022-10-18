#!/usr/bin/python
import csv, sys
import time
from PQ import PriorityQueue











stateToNum = {}
numToState = {}

def addedge(g,x, y, cost):
    g[x].append((y, cost))


with open('driving.csv', newline='') as csvfile:
    reader = list(csv.reader(csvfile))
    v = len(reader)-1
    graph = [[] for i in range(v)]
    costList = [[0 for x in range(v)] for y in range(v)]
    for i in range(0, len(reader)-1):
        temp = []
        for j in range(0,len(reader[i])-1):
            cost = reader[i+1][j+1]
            if (int(cost) > 0):
                addedge(graph,i,j,cost)
            costList[i][j]=cost
        stateToNum[reader[i+1][0]] = i
        numToState[i] = reader[i+1][0]
    
with open('straightline.csv', newline='') as csvfile:
    reader1 = list(csv.reader(csvfile))
    v = len(reader1)-1
    slGraph = [[] for i in range(v)]
    for i in range(0, len(reader1)-1):
        for j in range(0,len(reader1[i])-1):
            cost = reader1[i+1][j+1]
            addedge(slGraph,i,j,cost)


def best_first_search(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    order = []
    pq.insert((0, actual_Src,numToState[actual_Src],costList[actual_Src][actual_Src]))
    visited[actual_Src] = numToState[actual_Src]
    while pq.isEmpty() == False:
        smf = pq.delete()
        u = smf[1]
        order.append(numToState[u])
        if u == target:
            break
        
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = numToState[u]
                pq.insert((slGraph[v][target][1], v,numToState[v],costList[u][v]))
        
            
   
    order.reverse()
    path = []
 
    
    curr = visited[target]
    for x in order:
        path.append(curr)
        if(stateToNum[curr] == actual_Src):
            break
        curr = visited[stateToNum[path[len(path)-1]]]
       
    path.reverse()
    
    path.append(numToState[target])
    
    
    cost = 0
    for i in range(1,len(path)):
        if (i!=0):
            cost = cost + int(costList[stateToNum[path[i-1]]][stateToNum[path[i]]])
    return((path,cost))
    

def A(actual_Src, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    order = []
    pq.insert((0, actual_Src))
    visited[actual_Src] = (numToState[actual_Src],0)
    
    while pq.isEmpty() == False:
        smf = pq.delete()
        u = smf[1]
        order.append(numToState[u])
        if u == target:
            break
        prevCost = int(visited[u][1])
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = (numToState[u],int(costList[u][v])+prevCost)
                totalVal = int(slGraph[v][target][1])+(int(costList[u][v])+visited[u][1])
                #totalVal = (int(costList[u][v])+visited[u][1])
                pq.insert((totalVal, v,numToState[v],costList[u][v],slGraph[v][target][1]))
                if v == target:
                    break
                
    path = []
    curr = visited[target][0]
    for x in order:
        path.append(curr)
        if(stateToNum[curr] == actual_Src):
            break
        curr = visited[stateToNum[path[len(path)-1]]][0]
        
       
    path.reverse()
    path.append(numToState[target])
    
    
    cost = 0
    for i in range(1,len(path)):
        if (i!=0):
            cost = cost + int(costList[stateToNum[path[i-1]]][stateToNum[path[i]]])
    
    return((path,cost))
    


def printResult(result,time,isBsf):
    if(result[0] != []):
        if isBsf:
            print("Greedy Best First Search:\nSolution path: ",end="")
            print(result[0],end="")
            print()
            print("Number of states on a path: " + str(len(result[0])))
            print("Path cost: " + str(result[1]))
            print("Execution time: " + str(time))
            print()
            return
        print("A* Search:\nSolution path: ",end="")
        print(result[0],end="")
        print()
        print("Number of states on a path: " + str(len(result[0])))
        print("Path cost: " + str(result[1]))
        print("Execution time: " + str(time))
        return
    if isBsf:
        print("Greedy Best First Search:\nSolution path: ",end="")
        print("[NOT FOUND]",end="")
        print()
        print("Number of states on a path: N/A miles")
        print("Path cost: 0 miles")
        print("Execution time: " + str(time))
        print()
        return
    print("A* Search:\nSolution path: ",end="")
    print("[NOT FOUND]",end="")
    print()
    print("Number of states on a path: N/A miles")
    print("Path cost: 0 miles")
    print("Execution time: " + str(time))
    return

if __name__ == "__main__":

    if(len(sys.argv) != 3):
        print("ERROR: Not enough or too many input arguments.")
        exit(1)
    
    try:
        src = stateToNum[sys.argv[1]]
    except Exception as e:
        printResult([],0,True)
        printResult([],0,False)
        exit()
    try:
        dest = stateToNum[sys.argv[2]]
    except Exception as e:
        printResult(([],0),0,True)
        printResult(([],0),0,False)
        exit()

    
    print("Dass, Rishon, A20443042 solution:\nInitial state: " + sys.argv[1] + "\nGoal state: " + sys.argv[2])
    startTime = time.time()
    try:
        bsfResult = best_first_search(src, dest, v)
        printResult(bsfResult,time.time()-startTime,True)
    except Exception as e:
        printResult([],0,True)
    
    startTime = time.time()
    try:
        aResult = A(src,dest,v)
        printResult(aResult,time.time()-startTime,False)
    except Exception as e:
        printResult([],0,False)
    
    
