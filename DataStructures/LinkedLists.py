__author__ = 'Mohammad'

import random
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

    def add_to_end(self,val):
        n= Node(val)
        if self.head is None:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n

    def add_node(self,n):
        if self.tail == self.head == None:
            self.tail = self.head =None
        else:
            self.tail.next = n
            self.tail = n

    def create_linked_list(self,lst):
        for item in lst:
            self.add_to_end(item)

    def __str__(self):
        n = self.head
        to_str = []
        while n != None:
            to_str.append(str(n.value))
            n = n.next
        return ' --> '.join(to_str)

    def clear(self):
        self.head =self.tail = None

    def introduce_loop(self, node_id):
        '''
        introduces a loop at node_id-th  node from the head
        '''
        n = self.head
        e = self.tail
        while node_id > 0:
            n = n.next
            node_id -= 1
        e.next = n
        print ("loop start: %d"% n.value)

    def find_loop(self):
        """
        Given a linked list, detect the starting node for a loop in that list if a loop exists
        Time Complexity is O(n)
        Space Complexity is O(1)
        """
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

    def find_kth_node_from_end(self, k):
        """
        Given a linked list, find 'n'th node from the end for a given value of n (n > 0)
        idea: make 1 pointer move k nodes and then move both 1 node
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

    def delete_node_with_value(self, val):

        while self.head.value == val:
            self.head = self.head.next

        curr_node = self.head
        next_node = self.head.next
        while next_node is not None:
            if next_node.value == val:
                curr_node.next = next_node.next
                next_node = curr_node.next
            else:
                curr_node = curr_node.next
                next_node = next_node.next

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

    def reverse_iterative(self):
        """
        Time Complexity is O(n)
        Space Complexity is O(1)
        """
        prev_node = None
        curr_node = None
        next_node = self.head
        while next_node is not None:
            curr_node = next_node
            next_node = next_node.next
            curr_node.next = prev_node
            prev_node = curr_node
        self.head = curr_node

    def reverse_recursive(self):
        """
        Given a linked list having n nodes. Reverse the list using recursive approach.
        Time Complexity is O(n)
        Space Complexity is O(1)
        """
        def reverse_rec(curr_node):
            if curr_node is not None:
                next_node = curr_node.next
                if self.head is not curr_node:
                    curr_node.next = self.head
                    self.head = curr_node
                else:
                    curr_node.next = None

                reverse_rec( next_node )

        reverse_rec(self.head)

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

    def merge_sorted(self, ll2):
        """
        Given 2 sorted linked lists, merge the lists to a single sorted linked list.
        Time Complexity is O(n+m)
        Space Complexity is O(1)
        """
        n1 = self.head
        n2 = ll2.head
        if n1.value <= n2.value:
            self.head = n1
            n1 = n1.next
        if n1.value > n2.value:
            self.head = n2
            n2 = n2.next
        merged_next = self.head
        while n1 is not None and n2 is not None:
            if n1.value <= n2.value:
                merged_next.next = n1
                n1 = n1.next
            else:
                merged_next.next = n2
                n2 = n2.next
            merged_next = merged_next.next

        if n1 is not None:
            merged_next.next = n1
        else:
            merged_next.next = n2

    def delete_duplicates_from_sorted_list_leaving_unique(self):
        """
        Given a sorted linked list, delete all duplicates such that each element appear only once.
        """
        curr_node = self.head
        next_node = curr_node.next

        while next_node is not None:
            if curr_node.value == next_node.value:
                next_node = next_node.next
            else:
                curr_node.next = next_node
                curr_node = next_node
                next_node = next_node.next
        curr_node.next = None

    def delete_duplicates_from_sorted_list(self):
        """
        Given a sorted linked list, delete all nodes that have duplicate numbers,
        leaving only distinct numbers from the original list.
        """
        n = Node(100)
        n.next = self.head
        curr_node = n
        next_node = curr_node.next

        while curr_node.next is not None and curr_node.next.next is not None:
            if curr_node.next.value == curr_node.next.next.value:
                duplicate = curr_node.next.value
                while curr_node.next is not None and curr_node.next.value == duplicate:
                    curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

    def is_palindrome(self):
        """
        Given a singly linked list, determine if it is a palindrome.
        Soln1: create a new list in reversed order and then compare each node. The time and space are O(n).
        Soln2: use a fast and slow pointer to get the center of the list,
               then reverse the second list and compare two sublists. The time is O(n) and space is O(1).
        """
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        mid_head = slow_ptr

        p1 = mid_head
        p2 = mid_head.next

        # reverse second half of the list
        while p1 is not None and p2 is not None:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        mid_head.next = None

        # compare the 2 halves

        first_head =  self.head
        mid_head = p1


        while first_head is not None and mid_head is not None:
            if first_head.value == mid_head.value:
                first_head = first_head.next
                mid_head = mid_head.next
            else:
                print("Not Palindrom")
                return
        print("Palindrome")







    def find_intersection(self):pass

    def sort(self):
        """
        Time Complexity of Solution: O(n*log n).
        Description: Sort the elements in this linked list in ascending order.
        Technical Details: Sorting a LinkedList in place is very costly:
        in the order of O(n^2# log(n)) with a good algorithm.
        Therefore it makes sense to create an array from the list,
        sort the array, and then empty the array into the list by
        index. It's kind of like: unbutton a shirt; move the buttons
        around; then button the shirt anew. (I think it's a good analogy.)
        http://www.geekviewpoint.com/python/singly_linked_list/counting_sort
        """
        pass


    def swap_elements(self):
        """
        http://www.geekviewpoint.com/python/singly_linked_list/swap_elements
        """
        pass




def add_linked_lists(head1, head2):
    """
    Time Complexity is O(n)
    """

    def count_diff(head1, head2):
        extra_nodes = 0
        temp = head1
        while temp is not None:
            extra_nodes += 1
            temp = temp.next
        temp = head2
        while temp is not None:
            extra_nodes -= 1
            temp = temp.next
        return extra_nodes

    def add_lists(node1, node2, extra_node, carry, head1, head2):
        if node1 is None and node2 is None:
            carry = 0
            return None
        next_node = Node()
        if extra_nodes > 0:
            next_node = add_lists(node1.next, None, extra_node - 1,  carry, head1, head2)
        elif extra_nodes < 0:
            next_node = add_lists(None, node2.next, extra_node + 1, carry, head1, head2)
        else:
            node1_next =head1 if node1 is None else node1.next
            node1_next =head2 if node2 is None else node2.next
            next_node = add_lists(None, node2.next, extra_node + 1, carry, head1, head2)



    if head1 is None: return head2
    if head2 is None: return head1
    extra_nodes = count_diff(head1, head2)
    carry = None
    if extra_nodes > 0:
        result, carry = add_lists(head1, None, extra_nodes - 1, carry, head1, head2);
    elif extra_nodes < 0:
        result, carry = add_lists(None, head2, extra_nodes + 1, carry, head1, head2);
    else:
        result, carry = add_lists(head1, head2, 0, carry, head1, head2);

    if carry != 0:
        temp_node = SinglyLinkedList
        temp_node.add_to_front(carry)
        temp_node.next = result
        result = temp_node




    # add_linked_lists(ll1.next, ll2.next)


    pass

def test_delete_node_with_value():
    lla = SinglyLinkedList()
    llb = SinglyLinkedList()

    lla.add_to_front(5)
    lla.add_to_front(5)
    lla.add_to_front(7)
    lla.add_to_front(6)
    lla.add_to_front(5)
    lla.add_to_front(5)
    lla.add_to_front(5)
    lla.add_to_front(5)
    lla.add_to_front(4)
    lla.add_to_front(5)
    lla.add_to_front(3)
    lla.add_to_front(2)
    lla.add_to_front(5)
    lla.add_to_front(1)
    lla.add_to_front(5)
    lla.add_to_front(5)
    lla.add_to_front(5)
    lla.add_to_front(5)

    print(lla)
    lla.delete_node_with_value(5)
    print(lla)



# lla.reverse_pairs()
# print (lla)

# a_node = Node(3)
# lla.add_after_node(a_node, 14)
# a_node = Node(1)
# lla.add_after_node(a_node, 15)

def test_find_loop():
    lla = SinglyLinkedList()
    lla.create_linked_list([i for i in range(10)])
    lla.introduce_loop(3)
    lla.find_loop()

def test_find_kth_node_from_end():
    lla = SinglyLinkedList()
    lla.add_to_end(1)
    lla.add_to_end(2)
    lla.add_to_end(3)
    lla.add_to_end(4)
    lla.add_to_end(5)
    lla.add_to_end(6)
    lla.add_to_end(7)
    lla.find_kth_node_from_end(4)

def test_reverse_iterative():
    lla = SinglyLinkedList()
    lla.create_linked_list([1, 2, 3, 4, 5, 6])
    print (lla)
    lla.reverse_iterative()
    print (lla)

def test_reverse_recursive():
    lla = SinglyLinkedList()
    lla.create_linked_list([1, 2, 3, 4, 5, 6])
    print (lla)
    lla.reverse_recursive()
    print (lla)

def test_merge_sorted_ll():
    lla = SinglyLinkedList()
    llb = SinglyLinkedList()
    lla.create_linked_list([1, 3, 4, 12, 18, 19])
    llb.create_linked_list([7, 9, 10, 15, 18, 20])
    print (lla)
    print (llb)
    lla.merge_sorted(llb)
    print (lla)

def test_delete_duplicates_from_sorted_list_leaving_unique():
    lst = [random.randint(0, 10) for i in range(20)]
    lst.sort()
    print (lst)
    lla = SinglyLinkedList()
    lla.create_linked_list(lst)
    print(lla)
    lla.delete_duplicates_from_sorted_list_leaving_unique()
    print(lla)

def test_delete_duplicates_from_sorted_list():
    lst = [random.randint(0, 15) for i in range(10)]
    lst.sort()
    print (lst)
    lla = SinglyLinkedList()
    lla.create_linked_list(lst)
    print(lla)
    lla.delete_duplicates_from_sorted_list()
    print(lla)

def test_is_palindrome():
    lla = SinglyLinkedList()
    lla.create_linked_list([1,  3,4, 3, 1])
    print (lla)
    lla.is_palindrome()

# test_reverse_iterative()
# test_reverse_recursive()
# test_delete_node_with_value()
# test_merge_sorted_ll()
# test_delete_duplicates_from_sorted_list_leaving_unique()
# test_delete_duplicates_from_sorted_list()
# test_is_palindrome()