from PQ import PriorityQueue

#('390', 28, 'NH') ('332', 37, 'RI') ('417', 44, 'VT') ('126', 29, 'NJ') ('91', 36, 'PA')

pq = PriorityQueue()
pq.insert(('390', 28, 'NH'))
pq.insert(('332', 37, 'RI'))
pq.insert(('417', 44, 'VT'))
pq.insert(('126', 29, 'NJ'))
pq.insert(('91', 36, 'PA'))

print(pq.delete())


 
