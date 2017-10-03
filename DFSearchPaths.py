graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#graph={ 0:[1,3,4], 1:[0,2,4], 2:[1,6],3:[0,4,6], 4:[0,1,3,5], 5:[4], 6:[2,3] }
##graph=[[1,3,4], [0,2,4], [1,6], [0,4,6], [0,1,3,5], [4], [2,3] ]

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]  #1st start - vertex and 2nd start is path

   	while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path): #set(path) - made path
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
# print(list(bfs_paths(graph, 'A', 'F')))
#1st iteration queue = [('A',['A'])] => (vertex, path) = ('A',['A']) => queue = [('B', ['A', 'B'] ), ('C', ['A', 'C'])]
#2nd iteration queue = [('B', ['A', 'B'] ), ('C', ['A', 'C'])] => (vertex, path) = ('B',['A', 'B']) => queue = [('C', ['A', 'C']), ('D', ['A', 'B', 'D']), ('E', ['A', 'B', 'E'])]
#3rd iteration queue = [('C', ['A', 'C']), ('D', ['A', 'B', 'D']), ('E', ['A', 'B', 'E'])] => (vertex, path) = ('C',['A', 'C'])=> queue = [('D', ['A', 'B', 'D']), ('E', ['A', 'B', 'E'])] =>  yield ['A', 'C', 'F']
#4th iteration queue = [('D', ['A', 'B', 'D']), ('E', ['A', 'B', 'E'])] => (vertex, path) = ('D', ['A', 'B', 'D']) => queue = [('E', ['A', 'B', 'E'])]
#5th iteration queue = [('E', ['A', 'B', 'E'])] => (vertex, path) = ('E', ['A', 'B', 'E']) => queue = [ ] => yield ['A', 'B', 'E', 'F']

# generates [['A', 'C', 'F'], ['A', 'B', 'E', 'F'] ] from 3rd and 5th iterations



def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path): #set(path) - made path
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
