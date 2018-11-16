#binary search tree implemented by python
#binary search tree traversal: O(n)
class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
    
    def get(self):
        return self.val
    
    def set(self, val):
        self.val = val
    
    def get_child(self):
        child = []
        if(self.left_child != None):
            child.append(self.left_child)
        if(self.right_child != None):
            child.append(self.right_child)
        return child
    
class BST:
    def __init__(self):
        self.root = None
    
    def set_root(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root != None):
            self.insert_node(self.root, val)
        else:
            self.set_root(val)
    
    def insert_node(self, current_root, val):
        #left child
        if(val <= current_root.get()):
            if(current_root.left_child):#has left child
                self.insert_node(current_root.left_child, val)
            else:#empty
                current_root.left_child = Node(val)
        #right child
        else:
            if(current_root.right_child):#has right child
                self.insert_node(current_root.right_child, val)
            else:#empty
                current_root.right_child = Node(val)
    
    def create_tree(self, arr):
        for val in arr:
            self.insert(val)
    
    def search_node(self, current_root, val):
        if current_root is None:
            return []
        if current_root.get() == val:
            return [current_root.get(), [x.get() for x in current_root.get_child()]]
        elif current_root.get() > val:
            return self.search_node(current_root.left_child, val)
        else:
            return self.search_node(current_root.right_child, val)

    def find_min_node(self, current_root):
        if(current_root.left_child):
            self.find_min_node(current_root.left_child)
        else:
            print(current_root.get())
    
    def find_max_node(self, current_root):
        if(current_root.right_child):
            self.find_max_node(current_root.right_child)
        else:
            print(current_root.get())
    
    def hubbard_deletion():
        pass


    #depth-first traversal
    #left -> current -> right ==> sorted order
    def in_order_print(self,node):
        if node:
            self.in_order_print(node.left_child)
            print(node.val)
            self.in_order_print(node.right_child)

    #current node -> left child -> right child
    def pre_order_print(self, node):
        if node:
            print(node.get())
            self.pre_order_print(node.left_child)
            self.pre_order_print(node.right_child)
    
    # left -> right -> current
    def post_order_print(self, node):
        if node:
            self.post_order_print(node.left_child)
            self.post_order_print(node.right_child)
            print(node.get())

    #breadth-first traversal:level by level
    def bft(self):
        queue = [self.root]
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.get())
            child = current_node.get_child()
            if(len(child)>0):
                for node in child:
                    queue.append(node)

if __name__ == '__main__':
    arr = [3,7,1,5,8,2]
    tree = BST()
    tree.create_tree(arr)
    # tree.insert(2)
    print('in order:')
    tree.in_order_print(tree.root)
    print('pre order:')
    tree.pre_order_print(tree.root)
    print('breadth-first traversal:')
    tree.bft()
    print('search:')
    print(tree.search_node(tree.root, 3))
    print('min value:')
    tree.find_min_node(tree.root)
    print('max value:')
    tree.find_max_node(tree.root)

