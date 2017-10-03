print ''
print 'ЗАДАНИЕ 2'
print 'Задан граф: связный неориентированный. Необходимо получить из этого графа остовное дерево, путем удаления ребер. Входные данные: m n (число вершин и кол-во ребер) (в данном случае 4 4)'
print '1 2 (пара вершин, задающая ребро)'
print '2 3 (пара вершин, задающая ребро)'
print '3 4 (пара вершин, задающая ребро)'
print '4 1 (пара вершин, задающая ребро)'
print 'Выходные данные:n-1 пара чисел - ребра построенного графа.Можете заметить, что дерево имеет n-1 ребро, где n - число вершин.'

class Edge:
  def __init__(self, vertex_a, vertex_b):
    self.x = vertex_a
    self.y = vertex_b

class Graph:
  def __init__(self, number_of_vertices):
    self.variety= [i for i in range(number_of_vertices)]
    self.graph = []
    self.tree = []

  def add_edges(self, number_of_edges):
    for i in range(number_of_edges):
      a = int(raw_input("Type the vertex connecting from "))
      b = int(raw_input("Type the vertex connecting to "))
      print type(a)
      if a in self.variety and b in self.variety:
        new_edge = Edge(a, b)
        self.graph.append(new_edge)
        print 'done'
      else:
        print 'invalid data'

    print 'end of function'

  def building_spanning_tree(self):
    for i in range(len(self.graph)):
      if len(self.tree) == len(self.variety) - 1:
        print 'tree is full'
        return self.tree
      a, b = self.graph[i].x, self.graph[i].y
      if self.variety[a] != self.variety[b]:
        self.tree.append(self.graph[i])
        old_variety, new_variety = self.variety[b], self.variety[a]
        for j in range(len(self.variety)):
          if self.variety[j] == old_variety:
            self.variety[j] = new_variety
    print 'completed building a spanning tree'
    return self.tree

  def show_the_spanning_tree(self):
    for edge in self.tree:
      print edge.x, " to ", edge.y



my_graph  = Graph(5)
print my_graph.variety
my_graph.add_edges(6)
my_graph.building_spanning_tree()
my_graph.show_the_spanning_tree()
