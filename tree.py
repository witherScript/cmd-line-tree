class Node:
  def __init__(self, data=None, child_left=None, child_right=None):
    self.data = data
    self.child_left = child_left
    self.child_right = child_right


# left child always smaller than parent
# right child always greater   
  def insert(self, value):
    value = value if isinstance(value, Node) else Node(value)
    if value is None or self is None:
      return self
    elif value.data<self.data and self.child_left is None:
      self.child_left = value
    elif value.data<self.data and self.child_left is not None:
      self.child_left.insert(value)
    elif value.data>self.data and self.child_right is None:
      self.child_right = value
    elif value.data>self.data and self.child_right is not None:
      self.child_right.insert(value)
    return self
  def __repr__(self):
    return f"""({self.data} = {self.child_left} {self.child_right})"""

root = Node(3)
root.insert(1)
root.insert(2)
print(root.insert(4))

# implement compiler to take string (3 = (1 = None None) None) -> constructs tree with the same implied properties
# ADR: sums total value in the tree 