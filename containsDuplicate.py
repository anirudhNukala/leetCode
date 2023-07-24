# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

# Example:
# Input: nums = [1,2,3,1]
# Output: true

nums = [1,1,1,3,3,4,3,2,4,2]

valid = False

for num in nums:
    if num in nums[(nums.index(num) + 1):]:
        valid = True
        break
    else:
        continue
    
if valid:
    print(True)
else:
    print(False)
    