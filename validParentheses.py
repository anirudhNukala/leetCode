# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example:
# Input: s = "()[]{}"
# Output: true

s = "{[]}"
sList = list(s)
validDict = {'(':')', '[':']', '{':'}'}
left = '([{'
right = ')]}'
lCount = 0
rCount = 0
for char in s:
    if char in left:
        lCount += 1
    elif char in right:
        rCount += 1