class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def __str__(self): # return nice value when call to print
        return str(self.data)

# add_to_tree_recursive method to create nodes
def add_to_tree(current_node, data):

    if current_node.data is None:
        current_node.data = data
    else:
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                add_to_tree(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                add_to_tree(current_node.right, data)


# findval method to compare the value with nodes
def findval(current_node, search_term):
    if current_node is None:
        return False
    elif search_term < current_node.data:
        if current_node.left is None:
            return False
        return findval(current_node.left, search_term)
    elif search_term > current_node.data:
        if current_node.right is None:
            return False
        return findval(current_node.right, search_term)
    else:
        return True
             

        
# Print the tree, using different traversal algorithms

def traverse_tree_in_order(current_node):
    if current_node is None:
        print("empty tree")
    else:
        if current_node.left is not None:
            traverse_tree_in_order(current_node.left)
        print( current_node.data)
        if current_node.right is not None:
            traverse_tree_in_order(current_node.right)

def traverse_tree_post_order(current_node):
    if current_node is None:
        print("empty tree")
    else:
        if current_node.left is not None:
            traverse_tree_post_order(current_node.left)
        if current_node.right is not None:
            traverse_tree_post_order(current_node.right)
        print( current_node.data)


def traverse_tree_breadth_first(current_node):
    if current_node is None:
        print("empty tree")
    else:
        node_q = []

        node_q.append(current_node)  # add to queue

        while len(node_q) > 0:
            current_node = node_q.pop(0) # get and remove front of queue
            if current_node.left is not None:
                node_q.append(current_node.left)
            if current_node.right is not None:
                node_q.append(current_node.right)
            print( current_node.data)

def dump_tree (current_node):
    if current_node is not None:
        print ('Data:', current_node.data, ' Left:', current_node.left, ' Right:', current_node.right)
        dump_tree(current_node.left)
        dump_tree(current_node.right)


def main():

    root = None # tree empty

    while True:

        choice = int(input ("""
1 to add data to tree
2 to dump tree structure
3 for depth first in-order traversal
4 for depth first post-order traversal
5 for breadth first in-order traversal
6 to search the tree for a term
99 to quit: """))

        if choice==1:
            data_for_tree=input("Enter item for tree (or hit enter to stop): ")

            while data_for_tree!="":
                if root is None: # create root
                    root = Node(data_for_tree)
                else:
                    add_to_tree(root, data_for_tree)
                data_for_tree=input("Enter item for tree (or hit enter to stop): ")
        elif choice == 2:
            dump_tree (root)
        elif choice == 3:
            traverse_tree_in_order(root)
        elif choice ==4:
            traverse_tree_post_order(root)
        elif choice ==5:
            traverse_tree_breadth_first(root)
        elif choice == 6:
            term = input("Enter a term to search for : ")
            result = findval(root, term)
            if result:
                print (term, 'found in tree')
            else:
                print (term, 'not found in tree')
                
        elif choice == 99:
            break
        
main()