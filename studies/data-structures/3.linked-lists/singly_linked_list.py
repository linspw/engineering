class Node:
  data = None
  next = None

  def __init__(self, data):
    self.data = data

  def __str__(self):
    return f"{self.data}"


class LinkedList:
  head: Node | None = None

  def insert(self, data):
    node = Node(data)

    if self.head:
      node.next = self.head
      self.head = node
    else:
      self.head = node

  def search_by_key(self, key):
    current = self.head
    while current:
      if current.data == key:
        return True
      current = current.next
    return False
  
  def remove_by_key(self, key):
      current = self.head
      prev = None

      while current and current.data == key:
        prev = current
        current = current.next
      
      if not current:
        print("Element is not present")
        return
      
      if prev:
        prev.next = current.next
      
      else: # if the element to be removed is the first 
        self.head = current.next


  def display(self):
    current = self.head
    while current:
      print(current, end=' => ' if current.next else None)
      current = current.next
  

linked_list = LinkedList()

linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)

print("Linked List:")

linked_list.display()

print(linked_list.search_by_key(2))

linked_list.remove_by_key(2)

linked_list.display()

