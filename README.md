# Tree CLI

## Description
A cli tool that takes a string BST as input and converts it into a tree in memory

### Commands
- parse [string] 
```
$ parse (3 None (5 None None))
```
parse [string] emits a tokenized representation of the input with whitespace removed

- tree [string]:
```
$ tree (3 None (5 None None))
```
tree [string] parses and Lexes the input, generating a BST from the user's input, uses the tree.py ```__repr__()``` method to display the tree's data

### Syntax

Parenthesis signify the beginning of a BST Node, all parentheses must be balanced. Internally, the REPL checks all parentheses using a stack. If the stack is not empty when the last opening parenthesis is found, an exception is thrown.

Here is how you would generate a BST with a root of 3 and two children: 1 and 4

$ tree (3 (1 None None) (4 None None))
