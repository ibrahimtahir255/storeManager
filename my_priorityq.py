"""A linked list implementation of priority queue.
Attributes:
  - head; PriorityNode or None if queue empty.
  - tail; PriorityNode or None if queue empty.
  - count; int; number of nodes in queue."""
class PriorityQueue:
  def __init__( self ):
    """Constructor to create an empty queue."""
    self.head = None
    self.tail = None
    self.count = 0
  
  def is_empty( self ):
    """Check to see if the queue is empty.
    Return: Boolean, True if empty, False otherwise."""
    return self.count == 0

  def __len__( self ):
    """Return the length (int) of the queue."""
    return self.count 

  def enqueue( self, item, priority ):
    """Insert the new node with item and priority into the queue.
    Parameters:
      - self; PriorityQueue
      - item; data to be stored in the node
      - priority; int; priority of the node
    Return: None"""
    new_node= PriorityNode(item,priority)
    if self.is_empty():
      self.head = new_node
      self.tail = new_node
    else:
      if self.head.priority > new_node.priority:
        new_node.next = self.head
        self.head = new_node
        # self.count = self.count + 1
      else:
        cur = self.head
        while cur != None and cur.priority <= new_node.priority:
          prev = cur
          cur = cur.next

        new_node.next = cur
        prev.next = new_node
    self.count = self.count + 1
        # return None 
    
  def dequeue( self ):
    """Remove an item at the front.
    Parameters: self; PriorityQueue.
    Return: data stored in front node."""
    
    # assert not self.is_empty(), "Cannot dequeue from an empty queue."
    # item = self.head
    # self.head = self.head.next
    # if self.head == None:   # now an empty queue
    #   self.tail = None
    # self.count -= 1
    # return item.data

    if self.is_empty() == True:
      return
    else:
      item = self.head
      self.head = self.head.next
      self.count = self.count-1
      return item.data 
    
  def peek( self ):
    """Examine the value of the first node.
    Parameter: self; PriorityQueue
    Return: data from front node."""
    # assert not self.is_empty(), "Cannot peek from an empty queue."
    # node = self.head
    # return node.data
    if self.is_empty() == True:
      return 
    else:
      return self.head.data
  def __str__(self):
    items = []
    cur = self.head
    while cur != None:
      items.append(cur.data)
      cur=cur.next
    return str(items)
    
        

class PriorityNode:
  """The node for a priority queue.
  Attributes:
    - data; information to store
    - priority; int; to order nodes. lower values are higher priority.
    - next; PriorityNode of next node or None if at end of queue."""
  def __init__( self, data, priority ):
    self.data = data
    self.priority = priority
    self.next = None

  def __str__( self ):
    """Return a string form of the node for printing."""
    value = 'Priority : ' + str( self.priority ) + \
        ' data: ' + str( self.data )
    return value



##############test############
pq= PriorityQueue()
pq.enqueue('white', 2)

print(pq)
print(len(pq))