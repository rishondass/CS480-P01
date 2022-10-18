import pandas
import time 
from collections import OrderedDict 
import re 
import sys

#Handle necesary arguments 
if len(sys.argv)!= 3:
    print ('ERROR: Not enough or too many input arguments.')
    exit (0)
else:
    FINAL_STATE = str(sys.argv [2])
    INITIAL_STATE = str(sys.argv[1])
    straightline_data = pandas.read_csv('straightline.csv', index_col=0, header=0).to_dict()
    driving_data = pandas.read_csv('driving.csv', index_col=0, header=0).to_dict()
    
    print ('Tony, Allam,A20423961, Answer: \n')
    print(f'Initial State : 85 (INITIAL_STATE)\n')
    print (f'Goal State : 85 {FINAL_STATE}\n')
    # Check if the inital and finals states are actually in the set of possible states
    if INITIAL_STATE not in straightline_data.keys() or FINAL_STATE not in straightline_data.keys():
        print ('CITY DOES NOT EXIST')
        print ('Solution path: FAILURE: NO PATH FOUND')
        print( 'Number of states on a path: 0')
        print('Path cost: 0')
        exit (0)
    else:
        start_t = time.perf_counter ()
        initial_set = set()
        for k in driving_data [INITIAL_STATE]:
            if driving_data [INITIAL_STATE] [k] > 0:
                initial_set.add((k, driving_data[INITIAL_STATE] [k]))
        final_set = set ()
        for k in driving_data [FINAL_STATE]:
            if driving_data [INITIAL_STATE] [k] > 0:
                final_set.add((k, driving_data[INITIAL_STATE] [k]))
        if len(initial_set) == 0 or len(final_set) == 0:
            end_t = time. perf_counter()
            print('Solution path: FAILURE: NO PATH FOUND')
            print( 'Number of states on a path: 0')
            print('Path cost: 0')
            print (f'Execution time : {(end_t - start_t)}')
            exit (0)
        if INITIAL_STATE == FINAL_STATE:
            print ('INITIAL AND FIÑAL STATES ARE BOTH EQUAL')
        else:
            def GBFS(starting_node, ending_node):
                curr_p = [starting_node]
                cost_p = []
                node = starting_node
                while curr_p:
                    path_g = []
                    for k in driving_data[node]:
                        if driving_data[node][k] > 0:
                            path_g.append([k, driving_data[node][k]])
                        neighbors = []
                        # Handles the list of neighbors of the current node
                        for k in range(len(path_g)):
                            neighbors.append ([path_g[k][0], path_g[k][1], straightline_data[ending_node][path_g[k][0]]])
                        neighbors = sorted(neighbors, key=lambda x: x[2])
                        node = neighbors [0] [0]
                        cost = neighbors [0] [1]
                        cost_p.append (node)
                        cost_p.append (cost)
                        if node == ending_node:
                            len_p = len(curr_p)
                            break
                        if len(curr_p) > len(straightline_data.keys):
                            curr_p = ('FAILURE: NO PATH FOUND')
                            cost_p = 0
                            break
                        return curr_p, cost_p, len_p
                start_time_t = time.perf_counter()
                (out, Path_cost, len_Path) = GBFS(INITIAL_STATE, FINAL_STATE)
                end_time_t = time.perf_counter()
                print ('Greedy Best First Search:')
                print (f'Solution path : {", ".join(out)}')
                print (f'number of states on the path: {len_Path}')
                print (f'path cost : {sum(Path_cost)}')
                print (f'Execution time : {(end_time_t - start_time_t)}')
                
                def a_star(starting_node, final_node):
                    def p_cost(curr_p):
                        cost_p = 0
                        for i in range(len(curr_p) - 1):
                            cost_P = cost_p+ driving_data[curr_p[i]][curr_p[i + 1]]
                        return cost_p
                    def remove_digit(input ):
                        res =''.join([i for i in input if not i.isdigit()])
                        return res
                    def remove_path(l):
                        sample = ' [0-9]'
                        output = [re.sub(sample, '', i) for i in l]
                        return output
                    curr_p = []
                    path_all = {}
                    path_all[starting_node] = [starting_node]
                    node = starting_node
                    opened_node = [starting_node]
                    visited = {}
                    
                    for keys in driving_data:
                        visited [keys] = {}
                        for keys1 in driving_data[keys]:
                            if driving_data[keys][keys1] > 0:
                                visited [keys][keys1] = driving_data[keys][keys1]
                    straight_line = straightline_data[final_node]
                    f_list = 0
                    while starting_node:
                        f_score = {}
                        curr_p = path_all[node]
                        h = 0
                        for i in range(len(curr_p) - 1):
                            h = h + visited [remove_digit(curr_p[j])][remove_digit(curr_p[j + 1])]
                        neighbors = visited [remove_digit(node)]
                        for k in neighbors.keys():
                            if k in path_all.keys ():
                                k = k + '1'
                            path_all[k] = path_all[node] + [k]
                            f_score[k] = h + neighbors [remove_digit(k)] + straight_line[remove_digit(k)]
                            
                        f_list.update(f_score)
                        f_test = (sorted(f_list.items(), key=lambda x: x [1]))
                        f_list = OrderedDict(f_test)
                        
                        if not node == starting_node:
                            del (f_list [node])
                        node = next(iter(f_list))
                        opened_node.append (node)
                        
                        # Check if the goal state is reached
                        if remove_digit (node) == final_node:
                            break
                        # Checks if an error will take place
                        if len(curr_p) > len(straightline_data.keys()):
                            cost_P = 0
                            curr_p = ['FAILURE: NO PATH FOUND']
                            Len_p = 0
                            break
                    # All outputs
                    out_p = path_all [node]
                    out_p = remove_path(out_p)
                    out_cost = p_cost(out_p)
                    p_len = len(out_p)
                    return out_p, out_cost, p_len
                #Prints the output and all the information about A*
                print ('\nA* Search:')
                start_t = time.perf_counter()
                (out, cost_p, len_p) = a_star (INITIAL_STATE, FINAL_STATE)
                end_t = time.perf_counter ()
                print(f'Solution path : {", , ".join(out)}')
                print(f'Number of states on a path: {len_p}')
                print(f'Path cost : {cost_p}')
                print(f'Execution time : {end_t - start_t}')