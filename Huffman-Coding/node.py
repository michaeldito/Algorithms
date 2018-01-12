class Node:  

  def __init__(self, key, value, left, right):
    self.key = key
    self.value = value
    self.left_child = left
    self.right_child = right

  def get_key(self):
    return self.key

  def get_left_child(self):
    return self.left_child

  def get_right_child(self):
    return self.right_child

  def __cmp__(self, other):
    return cmp(self.value, other.value)
  
  def __str__(self):
    return "({}, {})".format(self.key, self.value)