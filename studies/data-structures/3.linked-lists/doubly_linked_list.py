class Node:
  next = None
  prev = None
  data = None

  def __init__(self, data):
    self.data = data
  
  def __str__(self):
    return f"{self.data}"

class DoubleLinkedList:
  head: Node | None = None

  def __str__(self):
    return f"{self.data}"
  
  def insert(self, data):
    node = Node(data)

    if self.head:
      node.next = self.head
      self.head.prev = node
      self.head = node
    else:
      self.head = node

  def remove_by_key(self, data):
    current = self.head

    while current and current.data != data:
      current = current.next
  
    if not current:
      print("Element not found")
      return
    
    if current.prev:
      current.prev.next = current.next
    if current.next:
      current.next.prev = current.prev
    
    if not current.prev:
      self.head = current.next

  def display(self):
    current = self.head
    while current:
      print(current, end=' => ' if current.next else None)
      current = current.next


linked_list = DoubleLinkedList()

linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)


print("Double Linked List:")

linked_list.display()

linked_list.remove_by_key(2)

linked_list.display()

