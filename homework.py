print 'Реализовать ДЗ-7.2 на основе примера на C++. Файл в Skype (graphToTree.cpp)'


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

import math
print ''
print 'Даны две строки, содержащие целые числа (“33” и “444” например). Вычислить произведение этих чисел. Числа могут достигать до 100 разрядов.Указание: не использовать библиотеки BigInt'

def Solution(a,b):
  num1_list = []
  num2_list = []
  result = 0
  for i in range(len(a)):
    num1_list.append(int(a[i]+'0'*(len(a[i:])-1)))
  for j in range(len(b)):
    num2_list.append(int(b[j]+'0'*(len(b[j:])-1)))
  print 'list 1: ', num1_list
  print 'list 2: ', num2_list
  for i in range(len(num1_list)):
    for j in range(len(num2_list)):
      result = result + num1_list[i]*num2_list[j]
  return result

my_answer = Solution('10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', '1123123124214124636')



b = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*1123123124214124636

if my_answer == b:
  print "TRUE"
