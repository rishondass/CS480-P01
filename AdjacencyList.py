# Adjascency List representation in Python


class AdjNode:
    def __init__(self, value,cost):
        self.vertex = value
        self.cost = cost
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d,cost):
        node = AdjNode(d,cost)
        node.next = self.graph[s]
        self.graph[s] = node

        # node = AdjNode(s,cost)
        # node.next = self.graph[d]
        # self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 45

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 5)
    graph.add_edge(0, 28)
    graph.add_edge(0, 32)
    graph.add_edge(0, 37)
    graph.add_edge(0, 44)
    graph.print_agraph()