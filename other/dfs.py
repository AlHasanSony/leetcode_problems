#dfs


#Using a python dictionary to act as an adjacency list
graph = { #dictionary
    '5': ['3', '7'], #key: 5, value: [3, 7]
    '3': ['2','4'], #key: 3, value: [2, 4]
    '7': ['8'],  #key: 7, value: [8]
    '2': [],   #key: 2, value: []
    '4': ['8'], #key: 4, value: [8]
    '8': []   #key: 8, value: []
}
visited = set(); # visited stores the nodes that have been visited and set() is a python set      which is used for storing unique values

def dfs(visited, graph, node): #function for dfs
    if node not in visited:
        print(node) #print the node
        visited.add(node) #add node to visited
        for neighbor in graph[node]: #for each neighbor
            dfs(visited, graph, neighbor) #recursive call
            
print("Following is the Depth-First Search")
dfs(visited, graph, '5')
    
    


# Traversal means that visiting all the nodes of a graph which can be done through Depth-first search or Breadth-first search in python. Depth-first traversal or Depth-first Search is an algorithm to look at all the vertices of a graph or tree data structure. Here we will study what depth-first search in python is, understand how it works with its bfs algorithm, implementation with python code, and the corresponding output to it. 

# What is Depth First Search?
# What do we do once have to solve a maze? We tend to take a route, keep going until we discover a dead end. When touching the dead end, we again come back and keep coming back till we see a path we didn't attempt before. Take that new route. Once more keep going until we discover a dead end. Take a come back again… This is exactly how Depth-First Search works.

# The Depth-First Search is a recursive algorithm that uses the concept of backtracking. It involves thorough searches of all the nodes by going ahead if potential, else by backtracking. Here, the word backtrack means once you are moving forward and there are not any more nodes along the present path, you progress backward on an equivalent path to seek out nodes to traverse. All the nodes are progressing to be visited on the current path until all the unvisited nodes are traversed after which subsequent paths are going to be selected.

# DFS Algorithm
# Before learning the python code for Depth-First and its output, let us go through the algorithm it follows for the same. The recursive method of the Depth-First Search algorithm is implemented using stack. A standard Depth-First Search implementation puts every vertex of the graph into one in all 2 categories: 1) Visited 2) Not Visited. The only purpose of this algorithm is to visit all the vertex of the graph avoiding cycles.

# The DSF algorithm follows as:

# We will start by putting any one of the graph's vertex on top of the stack.
# After that take the top item of the stack and add it to the visited list of the vertex.
# Next, create a list of that adjacent node of the vertex. Add the ones which aren't in the visited list of vertexes to the top of the stack.
# Lastly, keep repeating steps 2 and 3 until the stack is empty.


# links 
# https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/tutorial/
# https://favtutor.com/blogs/depth-first-search-python
