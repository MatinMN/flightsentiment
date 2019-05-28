from collections import defaultdict
# Get the weighted graph
weighted_graph = open("weighted_graph.txt")

# Get the nicknames of the citis in a list
cities_file = open('cities.txt')


# # A class to represent the adjacency list of the node
# class AdjNode:
#     def __init__(self, data, city):
#         self.city = city
#         self.vertex = data
#         self.next = None

# # A class to represent a graph. A graph
# # is the list of the adjacency lists.
# # Size of the array will be the no. of the
# # vertices "V"


# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [None] * self.V

#     # Function to add an edge in an undirected graph
#     def addEdge(self, src, dest, srcCity, destCity):
#         # Adding the node to the source node
#         node = AdjNode(dest, destCity)
#         node.next = self.graph[src]
#         self.graph[src] = node

#         # Adding the source node to the destination as
#         # it is the undirected graph
#         node = AdjNode(src, srcCity)
#         node.next = self.graph[dest]
#         self.graph[dest] = node

#     # Function to print the graph
#     def print_graph(self):
#         for i in range(self.V):
#             print("Adjacency list of vertex {}\n head".format(str(i) + " " + cities[i] ), end="")
#             temp = self.graph[i]
#             while temp:
#                 print(" -> {}".format(str(temp.vertex) + " " + str(temp.city)), end="")
#                 temp = temp.next
#             print(" \n")


# Create a list for cities
cities = []
cities.append("")

# append the cities to the list
for city in cities_file:
    city = city.split(' ')
    cities.append(city[2])

# # print(cities)

# graph = Graph(11)

# # A Python program for Dijkstra's shortest
# # path algorithm for adjacency
# # list representation of graph

# # A Python program for Dijkstra's shortest
# # path algorithm for adjacency
# # list representation of graph

# Python program to print all paths from a source to destination.

# This class represents a directed graph
# # using adjacency list representation


class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'. 
	visited[] keeps track of vertices in current path. 
	path[] stores actual vertices and path_index is current 
	index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False]*(self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path)


# Create a graph given in the above diagram
graph = Graph(11)

# This code is contributed by Neelam Yadav


# Create the graph
for edge in weighted_graph:
    edge = edge.split(' ')
    vertex1 = int(edge[0])
    vertex2 = int(edge[1])
    print(str(vertex1) + " " + str(vertex2))
    srcCity = cities[vertex1]
    destCity = cities[vertex2]
    print(srcCity + " " + destCity)

    graph.addEdge(vertex1, vertex2)

s = 1
d = 9
print("Following are all different paths from %d to %d :" % (s, d))
graph.printAllPaths(s, d)

# graph.print_graph()
