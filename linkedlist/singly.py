# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def traverseAndPrint(head):
#   currentNode = head
#   while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
#   print("null")

# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# traverseAndPrint(node1)


class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

    
    
    def traverse(self):
        while self.next is not None:
            print(self.data, "->")
node1=Node(45)
node2=Node(50)
node3=Node(49)
node4=Node(50)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=None

current=node1
while current is not None:
    print(current.data, end="->")
    current=current.next
print("None")






