# Romain Tranchant
# CIS 103 Fundamentals of Programming
# Stack implementation


# Define a class for Stack
class Stack:
# Constructor to initialize the stack as an empty list
    def __init__(self):
# Initialize an empty list to represent the stack
        self.stack = []

# Method to push an item onto the stack
    def push(self, item):
# Add the item to the end of the list (top of the stack)
        self.stack.append(item)

# LIFO (Last-In-First-Out) method to remove and return the top item
    def pop(self):
# Check if the stack is not empty before trying to pop an item
        if not self.is_empty():
# Remove and return the last item of the list (top of the stack)
            return self.stack.pop()
# Return an error message if the stack is empty
        return "Error: Stack is Empty"

# Method to peek at the top item without removing it
    def peek(self):
# Check if the stack is not empty before trying to peek
        if not self.is_empty():
# Return the last item of the list (top of the stack) without removing it
            return self.stack[-1]
# Return an error message if the stack is empty
        return "Error: Stack is Empty"

# Method to check if the stack is empty
    def is_empty(self):
# Return True if the stack is empty, False otherwise
        return len(self.stack) == 0


# Create a new Stack object
stack = Stack()

# Print a message indicating the items being pushed onto the stack
print("Stacking the items: 10, 20, 30")

# Push items onto the stack
stack.push(10)  # Push 10 onto the stack
stack.push(20)  # Push 20 onto the stack
stack.push(30)  # Push 30 onto the stack

# Print the result of popping the top item
print("Popped item:", stack.pop())  # Output: 30

# Print the result of peeking at the top item
print("Top item:", stack.peek())  # Output: 20

# Print whether the stack is empty
print("Is the Stack empty?", stack.is_empty())  # Output: False

# Pop two items from the stack
print(f"Popped item: {stack.pop()}")  # Output: 20
print(f"Popped item: {stack.pop()}")  # Output: 10

# Print whether the stack is empty after removing 10 and 20
print("After removing 10 and 20, is the Stack empty?", stack.is_empty())  # Output: True

# Print a separator for better output readability
print("*****************************************")


# Matching Parentheses Example

# Function to check if parentheses are balanced in an expression
def is_balanced(expression):
    stack = Stack()  # Create a new Stack to track opening parentheses
    pairs = {')': '(', '}': '{', ']': '['}  # Dictionary of matching pairs of parentheses

# Iterate through each character in the expression
    for char in expression:
# If the character is an opening parenthesis, push it onto the stack
        if char in pairs.values():
            stack.push(char)
# If the character is a closing parenthesis
        elif char in pairs.keys():
# Check if the stack is empty or if the top item doesn't match the expected opening parenthesis
            if stack.is_empty() or stack.pop() != pairs[char]:
# If not balanced, return False
                return False
    return stack.is_empty()  # Return True if the stack is empty, indicating balanced parentheses


# Test the is_balanced function with two examples
print(f"Is the Stack balanced?: {is_balanced('{[()]}')}")  # Output: True
print(f"Is the Stack balanced?: {is_balanced('{[(])}')}")  # Output: False


# Convert Infix to Postfix

# Function to convert an infix expression to postfix notation
def infix_to_postfix(expression):
# Dictionary for operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
# Create a list to store the output in postfix order
    output = []
# Create a new Stack to hold operators temporarily
    stack = Stack()

# Iterate through each character in the expression
    for char in expression:
# If the character is an alphanumeric character (operand), add it to the output
        if char.isalnum():
            output.append(char)
# If the character is an operator
        elif char in precedence:
# Pop operators with higher or equal precedence from the stack to the output
            while not stack.is_empty() and precedence.get(stack.peek(), 0) >= precedence[char]:
                output.append(stack.pop())
# Push the current operator onto the stack
            stack.push(char)
# If the character is an opening parenthesis, push it onto the stack
        elif char == '(':
            stack.push(char)
# If the character is a closing parenthesis
        elif char == ')':
# Pop operators from the stack to the output until an opening parenthesis is encountered
            while stack.peek() != '(':
                output.append(stack.pop())
# Remove the opening parenthesis from the stack
            stack.pop()

# Pop any remaining operators from the stack to the output
    while not stack.is_empty():
        output.append(stack.pop())

# Return the output list as a string representing the postfix expression
    return ''.join(output)

# Test the infix_to_postfix function
print(infix_to_postfix("A*(B+C)"))  # Output: "ABC+*"
