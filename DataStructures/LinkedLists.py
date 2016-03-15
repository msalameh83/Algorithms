__author__ = 'Mohammad'


class Node():
    def __init__(self, val, next = None):
        self.value = val
        self.next = next


class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

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

    def add_to_front(self,val):
        n= Node(val)
        n.next = self.head
        self.head = n
        if self.size() == 1:
            self.tail = n

    def __str__(self):
        n = self.head
        to_str = []
        while n != None:
            to_str.append(str(n.value))
            n = n.next
        return ' --> '.join(to_str)


    def clear(self):
        self.head =self.tail =None

    def add_to_tail(self,v):
        self.tail.next = Node(v)
        self.tail = self.tail.next

    def add_after_node(self, x, val):
        new_node = Node(val)
        if self.tail == None or self.tail.value == x.value:
            self.add_to_tail(val)
        else:
            n = self.head
            while n != None:
                if n.value == x.value:
                    new_node.next = n.next
                    n.next = new_node
                n = n.next

    def find(self,val):
        x = self.head
        while  x != None:
            if x.value == val:
                return x
            x = x.next
        return None
    def reverse(self):
        pass
    def reverse_rec(self):
        pass

    def reverse_pairs(self):
        '''
        abcdefg = badcfeg
        '''
        n = self.head
        self.head = n.next
        while n.next != None:
            pair_a = n
            pair_b = n.next
            next_pair= pair_b.next
            pair_b.next = pair_a
            pair_a.next = next_pair
            n = next_pair

    def find_kth_from_tail(self):
        pass

    def rearrange_in_place(self,x, rt):
        pass
lla = SinglyLinkedList()
lla.add_to_front(7)
lla.add_to_front(6)
lla.add_to_front(5)
lla.add_to_front(4)
lla.add_to_front(3)
lla.add_to_front(2)
lla.add_to_front(1)

lla.reverse_pairs()
print (lla)

a_node = Node(3)
lla.add_after_node(a_node, 14)
a_node = Node(1)
lla.add_after_node(a_node, 15)


# print (lla)
#
# print (lla.head.value)
# print (lla.tail.value)
#
# sll2 = SinglyLinkedList()
