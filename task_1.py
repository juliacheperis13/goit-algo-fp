class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def mergeSort(self):
        self.head = self._mergeSort(self.head)

    def _mergeSort(self, h):
        if h == None or h.next == None:
            return h

        middle = self._getMiddle(h)
        next_to_middle = middle.next
        middle.next = None

        left = self._mergeSort(h)
        right = self._mergeSort(next_to_middle)

        sorted_list = self._sortedMerge(left, right)
        return sorted_list

    def _sortedMerge(self, a, b):
        result = None

        if a == None:
            return b
        if b == None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self._sortedMerge(a.next, b)
        else:
            result = b
            result.next = self._sortedMerge(a, b.next)
        return result

    def _getMiddle(self, head):
        if (head == None):
            return head

        slow = head
        fast = head

        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeLists(self, list):
        headA = self.head
        headB = list.head

        node = Node(0)

        tail = node
        while True:
            if headA is None:
                tail.next = headB
                break
            if headB is None:
                tail.next = headA
                break

            if headA.data <= headB.data:
                tail.next = headA
                headA = headA.next
            else:
                tail.next = headB
                headB = headB.next

            tail = tail.next
        self.head = node.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.insert_at_end(20)
    llist.insert_at_end(25)
    llist.insert_at_end(1)
    llist.insert_at_end(13)
    llist.insert_at_end(22)

    print("Linked listed:")
    llist.print_list()

    print("Sorted linked list:")
    llist.mergeSort()
    llist.print_list()

    llist_2 = LinkedList()
    llist_2.insert_at_end(77)
    llist_2.insert_at_end(55)
    llist_2.insert_at_end(11)

    print("Sorted linked list 2:")
    llist_2.mergeSort()
    llist_2.print_list()

    print("Merged linked list with another list:")
    llist.mergeLists(llist_2)
    llist.print_list()

    print("Reversed linked list:")
    llist.reverse()
    llist.print_list()
