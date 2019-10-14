from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # enqueue means we are adding to the back/tail of the DLL
        # we need to increment/increase storage by 1
        #self.storage.length += 1
        # use add_to_tail() to add the value in a new node
        # to the back/tail of the DLL
        self.storage.add_to_tail(value)

    def dequeue(self):
        # dequeue means we are subtracting/removing from the front/head of the DLL
        # we need to decrement/decrease storage by 1
        #self.storage.length -= 1
        # if there is no node in storage
        if self.storage.head == None:
            # return None
            return None

        else:
            # use remove_from_head() to delete the first node/the head
            self.storage.remove_from_head()

    def len(self):
        # return the size of the queue
        return self.size
