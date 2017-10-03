print ''
print 'ЗАДАНИЕ 2'
print 'Задан граф: связный неориентированный. Необходимо получить из этого графа остовное дерево, путем удаления ребер. Входные данные: m n (число вершин и кол-во ребер) (в данном случае 4 4)'
print '1 2 (пара вершин, задающая ребро)'
print '2 3 (пара вершин, задающая ребро)'
print '3 4 (пара вершин, задающая ребро)'
print '4 1 (пара вершин, задающая ребро)'
print 'Выходные данные:n-1 пара чисел - ребра построенного графа.Можете заметить, что дерево имеет n-1 ребро, где n - число вершин.'

class Vertex:
   def __init__(self, name):
    self.name = name
    self.neighbors = []
    self.color = 'black'
   def add_neighbor(self, name):
    if name not in self.neighbors:
      self.neighbors.append(name)
    else:
      return False

class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex ):
    if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
      self.vertices[vertex.name] = vertex
      return True
    else:
      return False

  def add_edge(self, v, u):
    if v.name in self.vertices and u.name in self.vertices:
      for key, value in self.vertices.items():
        if key == u.name:
          value.add_neighbor(v.name)
        if key == v.name:
          value.add_neighbor(u.name)
      return True
    else:
      return False

  def finding_spanning_tree(self, v):
    stack = []
    path = []
    v.color = 'red'
    print 'v.name: ', v.name
    path.append(v.name)
    for name in v.neighbors:
      stack.append(name)
    while stack:
      current_name = stack.pop()
      print 'current name: ',current_name
      current_vertex = self.vertices[current_name]
      current_vertex.color = 'red'
      path.append(current_name)
      for name in current_vertex.neighbors:
        vertex = self.vertices[name]
        if vertex.color == 'black' and vertex.name not in  stack:
          stack.append(name)
        elif vertex.color == 'red' and vertex.name != path[path.index(current_name)-1]:
          current_vertex.neighbors.pop(current_vertex.neighbors.index(vertex.name))
          vertex.neighbors.pop(vertex.neighbors.index(current_vertex.name))
          print 'Edge between ', current_vertex.name, 'and', vertex.name, 'deleted'

    print "reseting the colors of the vertexes..."
    for key, value in self.vertices.items():
      value.color = 'black'

    return  path

A = Vertex('1')
B = Vertex('2')
C = Vertex('3')
D = Vertex('4')
my_graph  = Graph()
my_graph.add_vertex(A)
my_graph.add_vertex(B)
my_graph.add_vertex(C)
my_graph.add_vertex(D)

my_graph.add_edge(A,B)
my_graph.add_edge(B,C)
my_graph.add_edge(C,D)
my_graph.add_edge(D,A)

# print my_graph.vertices
# print my_graph.vertices['1'].neighbors
print my_graph.finding_spanning_tree(A)




print ''
print 'ЗАДАНИЕ 3'
print 'Задан неориентированный граф способом, указанным в задании 2.'
print 'Выяснить, является ли граф связным.'


A_1 = Vertex('1')
B_1 = Vertex('2')
C_1 = Vertex('3')
D_1 = Vertex('4')
E_1 = Vertex('5')

my_graph_1  = Graph()

my_graph_1.add_vertex(A_1)
my_graph_1.add_vertex(B_1)
my_graph_1.add_vertex(C_1)
my_graph_1.add_vertex(D_1)

my_graph_1.add_edge(A_1,B_1)
my_graph_1.add_edge(B_1,C_1)
my_graph_1.add_edge(C_1,D_1)
my_graph_1.add_edge(D_1,A_1)

def Checking_Connectivity(graph, v):
  path = graph.finding_spanning_tree(v)
  print 'path: ', path
  if len(path) != len(graph.vertices):
      return 'Graph is disconnected!'
  else:
      return 'Graph is connected!'


print Checking_Connectivity(my_graph_1, A_1)

my_graph_1.add_vertex(E_1)
print Checking_Connectivity(my_graph_1, A_1)
