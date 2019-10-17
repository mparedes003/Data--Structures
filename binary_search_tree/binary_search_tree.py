class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        else:
            # go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
      # if root equals target
        if self.value == target:
            # return True
            return True
    # Look at the left side
        if self.left:
            # if left side contains target
            if self.left.contains(target):
                # return True
                return True
    # Look at the right side
        if self.right:
            # if right side conatins target
            if self.right.contains(target):
                # return True
                return True
    # otherwise, return False
        return False

    '''Another option'''
    '''def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            # go left
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:        
            if not self.right:
                return False
            else:
                return self.right.contains(target)'''

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # This function will print in this order
            # root->left->right until we have traversed the whole BST

        # start at node which is the root node
        # if you are at the root node
        if node:
            # print the value at that node
            print(node.self.value)

            # use in_order_print() on the left node by recursion
            in_order_print(node.self.left)

            # use in_order_print() on the left node by recursion
            in_order_print(node.self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
