# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct

# Example:
# Input: nums = [1,2,3,1]
# Output: true

nums = [1,2,3,4]

valid = 0
while(valid = 0):
    for num in nums:
        if num in nums[(nums.index(num) + 1):]:
            valid += 1
        else:
            continue
    
if valid:
    print(True)
else:
    print(False)
    