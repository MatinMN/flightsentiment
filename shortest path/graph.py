from collections import defaultdict
import haversine, json

# Get the graph
graph_file = open("graph.txt")

# Get the names of the citis in a list
cities = open('cities.json')
cities = json.load(cities)
cities = cities['data']['cities']


# A list to return all paths with distances
paths = {}

class Graph:

    count_paths = 1

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def printAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            print(path)
            newPath = list(path)
            if(len(path) > 3 and len(path) < 6):
                paths[self.count_paths] = newPath
                self.count_paths = self.count_paths + 1
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


# Create the graph
for edge in graph_file:
    edge = edge.split(' ')
    vertex1 = int(edge[0])
    vertex2 = int(edge[1])
    print(str(vertex1) + " " + str(vertex2))
    # print(srcCity + " " + destCity)

    graph.addEdge(vertex1, vertex2)

s = 1
d = 9
print("Following are all different paths from %d to %d :" % (s, d))

graph.printAllPaths(s, d)

print(paths)