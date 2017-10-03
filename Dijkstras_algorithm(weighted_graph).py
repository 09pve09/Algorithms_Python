from queue import *

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = PriorityQueue()
		self.distance = sys.maxint
		self.color = 'black'

	def add_neighbor(self, v, weight):
		if v.name not in [x[1] for x in self.neighbors.queue]:
		  self.neighbors.put((weight, v.name))
		else:
		  return False

class Graph:
	vertices = {}


	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False




	def add_edge(self, u, v, weight):
	  if u.name in self.vertices and v.name in self.vertices:
	    for key, value in self.vertices.items():
	      if key == u.name:
	        value.add_neighbor(v, weight)
	      if key == v.name:
	        value.add_neighbor(u, weight)
	    return True
	  else:
	    return False

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))


def Dijkstras_algorithm(graph, vert):
    print 'STARTING Dijkstras_algorithm...'
    q = list()
    vert.distance = 0
    vert.color = 'red'
    print 'neighbors: ',vert.neighbors
    for v in vert.neighbors.queue:
      graph.vertices[v[1]].distance = vert.distance + v[0]
      q.append(v[1])

    while len(q) > 0:
      u = q.pop(0)
      vertex_u = graph.vertices[u]
      print 'current Vertex: ', vertex_u.name
      print 'its neighbors: ', vertex_u.neighbors.queue
      vertex_u.color = 'red'

      for v in vertex_u.neighbors.queue:
        vertex_v = graph.vertices[v[1]]
        if vertex_v.color == 'black' and v not in q:
          q.append(v[1])
        if vertex_v.distance > vertex_u.distance + v[0]:
          print 'vertex_v.distance: ', vertex_v.distance
          print 'vertex_u.distance + v[0]: ', vertex_u.distance + v[0]
          vertex_v.distance = vertex_u.distance + v[0]
          print ''


my_graph  = Graph()
A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
my_graph.add_vertex(A)
my_graph.add_vertex(B)
my_graph.add_vertex(C)
my_graph.add_vertex(D)
my_graph.add_vertex(E)

my_graph.add_edge(A, B,2)
my_graph.add_edge(A,C,4)
my_graph.add_edge(A,D,5)
my_graph.add_edge(B,C,1)
my_graph.add_edge(C,D,1)
my_graph.add_edge(C,E,1)
my_graph.add_edge(D,E,2)

Dijkstras_algorithm(my_graph, A)

for key in my_graph.vertices:
  print my_graph.vertices[key].name, 'To A:' ,my_graph.vertices[key].distance
  
