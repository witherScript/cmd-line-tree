from collections import namedtuple
from enum import Enum
from tree import *
# implement compiler to take string (3 (1 None None) None) -> constructs tree with the same implied properties
# ADR: sums total value in the tree 

class NewEnum(Enum):
  def __eq__(self, b):
    if isinstance(b, str):
      return self.name==b
    else:
      return self.name == b.name

  def __hash__(self):
    return id(self.name)
TokenInfo = namedtuple('TokenInfo', ["name", "value"])
EOF = "EOF"
ILLEGAL = "ILLEGAL"


Token = NewEnum("Token", [
  "OPEN", #(
  "CLOSE", #)
  "INT",
  "NONE"
])
"""
(2) -> Node(2)

(2 (1 None None) None)

-> push (
  -> push 2
    -> push (
      -> push 1
        -> push None
          -> push None
            -> push )
              -> push None
                -> push )
"""



class Lexer:
  def __init__(self, input_data) -> None:
    self.input: str = input_data
    self.pos: int = 0
    self.ch: str = ""
    self.read_char()

  def read_char(self) -> None:
    #read next char
    # update position
    if self.pos >= len(self.input):
      self.ch="\x00"
    else:
      self.ch=self.input[self.pos]
    self.pos += 1

  def __iter__(self):
    return self
  
  def lex_none(self):
      # Check if the next four characters form the word 'None'
      if self.input[self.pos:self.pos+4] == "None":
          # Extract the 'None' string
          data = self.input[self.pos:self.pos+4]
          # Advance the position by 4 to skip over 'None'
          self.pos += 4
          # Ensure the next character is read
          self.read_char()
          # Return the 'None' token
          return TokenInfo('NONE', data)

  def lex_int(self) -> TokenInfo:
    if is_digit(self.ch):
      pos = self.pos
      ttype = Token.INT.name
      while is_digit(self.ch):
        self.read_char()
      data = self.input[pos-1:self.pos-1]
      return TokenInfo(ttype, data)
  def lex_eol(self):
    if self.ch == '\x00':
      return TokenInfo(EOF, self.ch)
  def remove_whitespace(self):
    while is_whitespace(self.ch):
      self.read_char()
  def remove_comments(self):
    if self.ch=="#":
      self.read_char()
      while self.ch not in ["\n", "\r", "\x00"]:
        self.read_char()
  def lex_illegal(self):
    tok = TokenInfo("ILLEGAL", self.ch)
    self.read_char()
    return tok
    
  def lex_open_paren(self):
    if self.ch == "(":
      ch =  self.ch
      self.read_char()
      return TokenInfo("OPEN", ch)

  def lex_close_paren(self):
    if self.ch == ")":
      ch =  self.ch
      self.read_char()
      return TokenInfo("CLOSE", ch)

  def __next__(self)-> TokenInfo:
    if self.pos>len(self.input):
      raise StopIteration
    else:
      # checks for end of file, removes whitespace, comments, if nothing matches it is an illegal value, update position and return the token
      return self.lex_eol() \
      or self.lex_none() \
      or self.lex_int() \
      or self.remove_whitespace() \
      or self.remove_comments() \
      or self.lex_open_paren() \
      or self.lex_close_paren() \
      or self.lex_illegal()

def is_whitespace(char):
  return (char == " ") \
  | (char == "\t") \
  | (char == "\n") \
  | (char == "\r")

def is_digit(char):
  return ("0"<= char <= "9") \
       | (char == ".")
def is_paren(char):
  return char =="(" or char ==")"

