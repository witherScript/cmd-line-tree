from addr import *
from tree import *
import cmd


class Repl(cmd.Cmd):
  """A BST compiler"""
  def do_parse(self, line):
    """parse [input]
    Displays tokenized input
    """
    my_lex = Lexer(line)
    for tok in my_lex:
      print(tok)
    return my_lex
  
  def do_tree(self, line):
    """tree [legal tree]
      converts input string into a BST if parentheses are balanced
      ******EXAMPLE******
      input: (3 (2 None None) None) 
      Should convert into a tree where the root node contains
      the value 3 with a left child of 2 and a null right child
    """
    root = Node()
    stack = []
    whitespace = [' ', '\n', '\t', '\r']
    for char in line:
      if char == "(":
        stack.append(char)
      elif char not in whitespace and char.isnumeric():
        if root.data is None:
          root.data = int(char)
        else:
          root.insert(int(char))
      elif char == ")":
        stack.pop()
    if len(stack)>0:
      raise Exception("Illegal parentheses: check that all open parentheses literals ( have a corresponding closing literal )")
    print(root)
  def postloop(self):
    print
      

if __name__=="__main__":
  Repl().cmdloop()