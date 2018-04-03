class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None


#create a node 
root = Node('A')
n1 = Node('B')
n2 = Node('C')
n3 = Node('D')
n4 = Node('E')

#Set up children
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4

#Pre-Order Traversal
def pre_order(root,nodes):
    nodes.append(root.data)
    if root and root.left:
        pre_order(root.left,nodes)
    if root and root.right:
        pre_order(root.right,nodes)
    return nodes
print("Pre-order traversal gives:")
print(pre_order(root,[]))

#In-Order Traversal
def in_order(root,nodes):
    if root and root.left:
        in_order(root.left,nodes)
    nodes.append(root.data)
    if root and root.right:
        in_order(root.right,nodes)
    return nodes
print("In-order Traversal gives:")
print(in_order(root,[]))

#Post-order Traversal
def post_order(root,nodes):

    if root and root.left:
        pre_order(root.left,nodes)
    if root and root.right:
        pre_order(root.right,nodes)
        nodes.append(root.data)
    return nodes
print("Post-order Traversal gives:")
print(post_order(root,[]))

#Lever-Order Traversal
def level_order(root, nodes):
    queue = [root]
    while queue:
        n = queue.pop(0)
        nodes.append(n.data)
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
    return nodes
print("Level-order Traversal gives:")
print (level_order(root, []) )


