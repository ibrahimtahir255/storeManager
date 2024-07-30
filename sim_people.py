"""Used to store and manage information related to customers and cashiers."""

class StorePeople:
  """A generic class of store people from which customers and cashiers
  inherit properties.
  Attributes:
    id; int. unique identifier."""
  def __init__(self, id):
    self.id = id

# Add Cashier and Customer Class
class Cashier(StorePeople):
  def __init__(self, num, status=True):
    super().__init__(num)
    self.status = status 
    
    
class Customer(StorePeople):
  def __init__(self, id):
    super().__init__(id)
