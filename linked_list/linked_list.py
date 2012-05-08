class Node:

  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    return str(self.value)

class LinkedList:
  
  def __init__(self, node):
    self.head = node

  def add_to_list(self, node):
    current_node = self.head
    while(current_node.next):
      current_node = current_node.next 
    current_node.next = node

  def print_out_list(self):
    current_node = self.head
    while(current_node.next):
      print current_node.value
      current_node = current_node.next 
    print current_node.value
  
  def find_item_at(self, at_loc):
    current_node = self.head
    for var in range(at_loc-1):
      current_node = current_node.next 
    return current_node
node1 = Node("item 1")
node2 = Node("item 2")
node3 = Node("item 3")
node4 = Node("item 4")

ll = LinkedList(node1)  
ll.add_to_list(node2)
ll.add_to_list(node3)
ll.add_to_list(node4)

item_2 = ll.find_item_at(2)
print item_2
