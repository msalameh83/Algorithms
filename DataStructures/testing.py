from scipy.optimize.anneal import fast_sa

__author__ = 'Mohammad'

class Node():
    def __init__(self, val, next = None):
        self.value = val
        self.next = next

class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self,val):
        n= Node(val)
        n.next = self.head
        self.head = n
        if self.size() == 1:
            self.tail = n

    def add_to_end(self,val):
        n= Node(val)
        if self.head is None:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n

    def introduce_loop(self, node_id):
        n = self.head
        e = self.tail
        while node_id > 0:
            n = n.next
            node_id -= 1
        e.next = n
        print ("loop start: %d"% n.value)

    def find_kth_node_from_end(self, k):
        """
        Given a linked list, find 'n'th node from the end for a given value of n (n > 0)
        complexity is O(n) and extra space used is O(1).
        http://www.ideserve.co.in/learn/find-nth-node-from-the-end-of-linked-list
        """
        node1 = self.head
        node2 = self.head
        i = 0
        while i < k:
            node1 = node1.next
            i += 1
            if node1.next is None:
                print('%d is larger than length of LinkedList '%k)
                break
        if node1.next is not None:
            while node1 is not None:
                node1 = node1.next
                node2 = node2.next
            print('value of kth node from end is %d'%node2.value)
            return node2.value


    def find_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        loop = False
        while fast_ptr is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if fast_ptr is slow_ptr:
                print('Loop Found')
                loop = True
                break
        if loop is True:
            slow_ptr = self.head
            while slow_ptr is not fast_ptr:
                slow_ptr = slow_ptr.next
                fast_ptr = fast_ptr.next
            print (slow_ptr.value)

    def __str__(self):
        n = self.head
        to_str = []
        while n != None:
            to_str.append(str(n.value))
            n = n.next
        return ' --> '.join(to_str)

    def size(self):
        '''
        Time Complexity: O(n)
        '''
        n = self.head
        sz = 0
        while n != None:
            sz += 1
            n = n.next
        return sz

    def create_linked_list(self,lst):
        for item in list:
            self.add_to_end(item)
lla = SinglyLinkedList()
# lla.add_to_front(7)
# lla.add_to_front(6)
# lla.add_to_front(5)
# lla.add_to_front(4)
# lla.add_to_front(3)
# lla.add_to_front(2)
# lla.add_to_front(1)

lla.add_to_end(1)
lla.add_to_end(2)
lla.add_to_end(3)
lla.add_to_end(4)
lla.add_to_end(5)
lla.add_to_end(6)
lla.add_to_end(7)




# lla.introduce_loop(3)
# lla.find_loop()



print (lla)
lla.find_kth_node_from_end(10)







