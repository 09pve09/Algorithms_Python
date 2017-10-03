class Node:
  def __init__(self, val):
    self.value = val
    self.right = None
    self.left = None
  
class BST:
  def __init__(self):
    self.root = None
  
  def create(self, value):
    if self.root == None:
      self.root = Node(value)
    else:
      current = self.root
      while True:
        if value < current.value:
          if current.left:
            current = current.left
          else:
            current.left = Node(value)
            break
        elif value > current.value:
          if current.right:
            current = current.right
          else:
            current.right = Node(value)
            break
        else:
          break
  
        
def DFS(tree):
  if tree.root == None:
    return []
  
  visited, stack = set(), [tree.root]
  print "DFS TREE ROOT:", tree.root.value
  while stack:
    item = stack.pop()
    print
    visited.add(item)
    stack.extend(filter(None, [item.right, item.left]))
  return visited
    
        
tree = BST()
# tree.create(1)
nums = [1,2,3,4,5,6,7,8,9]
for i in nums:
  tree.create(i)
  
print DFS(tree)

for i in DFS(tree):
  print i.value
  
print 'root: ',tree.root.value
