class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # value is less than the root go left
        if value < self.value:
            # if there is no value on the left side
            if not self.left:
                # value becomes the root of the new subtree
                self.left = BinarySearchTree(value)
            else:
                # insert the the value
                self.left.insert(value)

        else:
            # go right
            # if there is no value on the right side
            if not self.right:
                # value becomes the root of the new subtree
                self.right = BinarySearchTree(value)
            else:
                # insert the the value
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
        # if there is no node on the right
        if not self.right:
            # return self.value
            return self.value
        # just keep moving to the right for as long as you can
        # return the node at the end of it all
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call the callbacl on self.value
        cb(self.value)

        # use for_each(cb) on the left through recursion
        if self.left:
            self.left.for_each(cb)

        # use for_each(cb) on the right through recursion
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # This function will print in this order
            # left->root->right until we have traversed the whole BST

        # start at node which is the root node
        # if you are at the root node
        if node:
            # use in_order_print() on the left node by recursion
            self.in_order_print(node.left)

            # print the value at that node
            print(node.value)

            # use in_order_print() on the left node by recursion
            self.in_order_print(node.right)

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
        # This function will print in this order
            # root->left->right until we have traversed the whole BST

        # start at node which is the root node
        # if you are at the root node
        if node:
            # print the value at that node
            print(node.value)

            # use pre_order_dft() on the left node by recursion
            self.pre_order_dft(node.left)

            # use pre_order_dft() on the left node by recursion
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
