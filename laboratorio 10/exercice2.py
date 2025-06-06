class Node:
    """Node for expression tree"""
    def __init__(self, value): # Contructor
        self.value = value
        self.left = None
        self.right = None
    
def build_expression_tree(postfix):
    stack = [] # Initialize an empty stack
    
    for token in postfix: # For each elment in the list "postfix"
        node = Node(token) # Create a new node and him value is "token"
        
        if token in ['+', '-', '*', '/']: # If token is an operator
            if stack:  # Safety check to ensure stack isn't empty
                # Asign the last element of the "stack" in node's right and delete it
                node.right = stack.pop()
            if stack:  # Safety check to ensure stack isn't empty
                # Asign the last element of the "stack" in node's left and delete it
                node.left = stack.pop()
        stack.append(node) # Store the "node" in the last position in "stack"
    
     # If stack isn't empty, it will return the first element of stack 
     # (root node of the expression tree),
     # else, return None
    return stack[0] if stack else None

# ✅ Test cases
# Test 1: Simple addition
# Input: 2 3 +
# Tree:    +
#         / \
#        2   3
tokens1 = ['2', '3', '+']
tree1 = build_expression_tree(tokens1)
print(tree1.value)
print(tree1.right.value)
print(tree1.left.value)
print(tree1.value == '+' and tree1.left.value == '2' and tree1.right.value == '3')  # 🌱 Simple tree

# Test 2: Complex expression
# Input: 2 3 4 * +
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
tokens2 = ['2', '3', '4', '*', '+']
tree2 = build_expression_tree(tokens2)
print(tree2.value == '+' and tree2.left.value == '2' and tree2.right.value == '*')  # 📊 Operator precedence

# Test 3: Nested operations
# Input: 1 2 + 3 4 - *
# Tree:    *
#         / \
#        +   -
#       / \ / \
#      1  2 3  4
tokens3 = ['1', '2', '+', '3', '4', '-', '*']
tree3 = build_expression_tree(tokens3)
print(tree3.value == '*' and tree3.left.value == '+' and tree3.right.value == '-')  # 🔗 Nested operations

# Test 4: Expression with variables
# Input: a b c * +
# Tree:    +
#         / \
#        a   *
#           / \
#          b   c
tokens4 = ['a', 'b', 'c', '*', '+']
tree4 = build_expression_tree(tokens4)
print(tree4.value == '+' and tree4.left.value == 'a' and tree4.right.value == '*')  # 🔤 Variable tree

# Test 5: More complex expression
# Input: a b + c d - /
# Tree:    /
#         / \
#        +   -
#       / \ / \
#      a  b c  d
tokens5 = ['a', 'b', '+', 'c', 'd', '-', '/']
tree5 = build_expression_tree(tokens5)
print(tree5.value == '/' and tree5.left.value == '+' and tree5.right.value == '-')  # 🧮 Complex tree