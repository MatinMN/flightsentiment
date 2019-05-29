from collections import defaultdict
from haversine import haversine
import json

# Get the graph
graph_file = open("graph.txt")

# Get the names of the citis in a list
cities = open('cities_with_id.json')
cities = json.load(cities)
cities = cities['data']['cities']

# A dictionary to return all paths with distances


class Graph:

    count_paths = 1
    all_paths = []
    paths = []
    sortPaths = []
    distances = []
    distances.append(0)

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def getAllPathsUtil(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)
        newPath = list(path)
        length = len(newPath)

        if (length > 1):
            srcIndex = newPath[length-2]
            destIndex = newPath[length-1]

            src = (cities[srcIndex]['lat'], cities[srcIndex]['long'])
            dest = (cities[destIndex]['lat'], cities[destIndex]['long'])
            # print (src)
            # print (dest)
            distance = haversine(src, dest)
            distance = distance + self.distances[len(self.distances)-1]
            self.distances.append(distance)
            # print (self.distances)

        # If current vertex is same as destination, then print current path[]
        if u == d:
            # print(path)
            if(len(path) > 3 and len(path) < 6):
                self.paths.append(newPath)
                newPath.append(int(self.distances[len(self.distances)-1]))
                sub_list = [self.count_paths, int(self.distances[len(self.distances)-1])]
                self.sortPaths.append(sub_list)
                self.count_paths = self.count_paths + 1
            else:
                newPath.append(int(self.distances[len(self.distances)-1]))
            self.all_paths.append(newPath)

        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.getAllPathsUtil(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        self.distances.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def getAllPaths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False]*(self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.getAllPathsUtil(s, d, visited, path)
    
    def getShortestPaths(self, src, dest):
        self.getAllPaths(src, dest)
        finalPaths = []
        # print (paths)
        self.sortPaths = sorted(self.sortPaths,key=lambda l:l[1], reverse=False)

        for sub_list in self.sortPaths:
            finalPaths.append(self.paths[sub_list[0]-1])
        
        return finalPaths
        # print (self.paths)
        # print (finalPaths)

    def getAllPossiblePaths(self):
        return self.all_paths

    def getNumberAllPaths(self):
        return len(self.all_paths)




# Initialize the graph
graph = Graph(11)

# Add edges to the graph
for edge in graph_file:
    edge = edge.split(' ')
    vertex1 = int(edge[0])
    vertex2 = int(edge[1])
    graph.addEdge(vertex1, vertex2)

# print (graph.getShortestPaths(1,9))
# print()
# print (graph.getAllPossiblePaths())
# print(paths)
