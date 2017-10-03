class Vertex(object):
	def __init__(self, n):
		self.name = n
		self.neighbors = list()

	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

  	def remove_neighbor(self, v):
    	if v in self.neighbors:
      	self.neighbors.pop( self.neighbors.index(v))


class Graph(object):
  vertices = {}
  def add_vertex(self, vertex):
    if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
      	self.vertices[vertex.name] = vertex
      	return True
	else:
		return False

  def add_edge(selv, u, v):
    if v.name in self.vertices and u.name in self.vertices:
      for key, value in self.vertices.items():
        if key == u.name:
          value.add_neighbor(v)
        if key == v.name:
          value.add_neighbor(u)
      return True
    else:
      return False

  def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))
