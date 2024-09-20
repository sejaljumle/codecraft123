# Function to insert an element at the bottom of a stack
def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

# Function to reverse the stack
def reverse_stack(stack):
    if stack:
        top = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, top)

# Test the function with the given example
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)