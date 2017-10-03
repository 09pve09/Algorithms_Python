
class Tree(object):
	def __init__(self, x,left=None,right=None):
		self.val = x
		self.left = left
		self.right = right







def levelOrder( root):
		if not root:
			return []
		ans, level = [], [root]
		while level:
			ans.append([node.val for node in level])
			temp = []
			for node in level:
				temp.extend([node.left, node.right])
			level = [leaf for leaf in temp if leaf]
		return ans

def insertVal(item,tree):
		if(item < tree.val):
			if(tree.left is not None):
				insertVal(item,tree.left)
			else:
				tree.left=Tree(item)
		else:
			if(tree.right is not None):
				insertVal(item,tree.right)
			else:
				tree.right=Tree(item)

def countOfChilds(root):
		count=1
		print ('Call...')
		if(root is not None):
			if(root.left is not None):
				count+=countOfChilds(root.left)
				print ('After left,count:'+str(count))
			if(root.right is not None):
				count+=countOfChilds(root.right)
				print ('After right,count:'+str(count))
		return count

t1=Tree(10)
insertVal(5,t1)
insertVal(15,t1)
insertVal(3,t1)
insertVal(8,t1)

a=levelOrder(t1)
print(a)
c=countOfChilds(t1)





print(c)
