from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # push means we are adding to the top/head of the DLL_Stack
        # we need to increment/increase size by 1
        self.size += 1
        # use add_to_head() to add the value in a new node
        # to the top/head of the DLL_Stack
        self.storage.add_to_head(value)

    def pop(self):
        # pop means we are subtracting/removing from the top/head of the DLL_Stack
        # if there is no node in storage
        if self.storage.head == None:
            # return None
            return None

        else:
            # we need to decrement/decrease size by 1
            self.size -= 1
            # use remove_from_head() to delete the last node added onto the DLL_Stack
            return self.storage.remove_from_head()

    def len(self):
        # return the size of the queue
        return self.size
