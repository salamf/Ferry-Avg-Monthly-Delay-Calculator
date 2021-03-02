class Node:
    def __init__(self, month, time_diff):

        self.month = month
        self.time_diff = [time_diff]

        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, month, time_diff):
        if self.head is None:
            self.head = Node(month, time_diff)
            return

        if self.head.month == month:
            self.head.time_diff.append(time_diff)
            return

        curr = self.head.next
        prev = self.head
        while curr is not None:

            if curr.month == month:
                curr.time_diff.append(time_diff)
                return

            prev = curr
            curr = curr.next

        prev.next = Node(month, time_diff)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.month)
            print(temp.time_diff)
            temp = temp.next
