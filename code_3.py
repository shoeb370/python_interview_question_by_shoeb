def is_balanced(s):
    stack = []
    matching_brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in matching_brackets.values():  # Opening brackets
            stack.append(char)
        elif char in matching_brackets:  # Closing brackets
            if not stack or stack.pop() != matching_brackets[char]:
                return False
    return not stack  # Returns True if stack is empty (all brackets are balanced)

# Test cases
print(is_balanced("{}"))        # True
print(is_balanced("()"))        # True
print(is_balanced("{[]}"))      # True
print(is_balanced("{[)]"))      # False
print(is_balanced("(]"))        # False
