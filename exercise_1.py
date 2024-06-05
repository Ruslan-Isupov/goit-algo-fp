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

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Function for reversing
  def reverse(self):
    cur = self.head
    prev = None
    
    while cur:
        next_node = cur.next        
        cur.next = prev      
        prev = cur
        cur = next_node        
    self.head = prev


# Function for insertion
  def insertion_sort(self):
   
    if self.head is None or self.head.next is None:
        return

    sorted_head = None
    cur = self.head

    while cur is not None:
        next_node = cur.next

        if sorted_head is None or sorted_head.data > cur.data:
            cur.next = sorted_head
            sorted_head = cur
        else:
            temp = sorted_head
            while temp.next is not None and temp.next.data < cur.data:
                temp = temp.next
            cur.next = temp.next
            temp.next = cur

        cur = next_node

    self.head = sorted_head
  

# Function for merging  
  def merge_sorted_lists(self,other):
  
    dummy_node = Node()
    current = dummy_node
    current1 = self.head
    current2 = other.head

    while current1 and current2:
        if current1.data < current2.data:
            current.next = current1
            current1 = current1.next
        else:
            current.next = current2
            current2 = current2.next
        current = current.next

    if current1:
        current.next = current1
    elif current2:
        current.next = current2

    self.head = dummy_node.next



llist1 = LinkedList()

llist1.insert_at_end(15)
llist1.insert_at_end(10)
llist1.insert_at_end(5)
llist1.insert_at_end(25)
llist1.insert_at_end(20)


print("Linked_list:")
llist1.print_list()

# Reversing
llist1.reverse()
print("Reversed_Linked_list:")
llist1.print_list()

# Sorting
llist1.insertion_sort()
print("Sorted_Linked_list1:")
llist1.print_list()


llist2 = LinkedList()
llist2.insert_at_end(25)
llist2.insert_at_end(13)
llist2.insert_at_end(6)
llist2.insert_at_end(27)
llist2.insert_at_end(19)

llist2.insertion_sort()
print("Sorted_Linked_list2:")
llist2.print_list()

# Merge Linked lists
llist1.merge_sorted_lists(llist2)
print("Merged_Sorted_Linked_lists:")
llist1.print_list()