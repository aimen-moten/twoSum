# Leetcode 1

# Algorithm
    # Create an empty hashmap
    # Loop through the array and check if target minus the current element exists in the hashmap
    # If it exists, return the index of those elements
    # Else add the current element to the hashmap

# Code:
def twoSum(nums: list[int], target: int) -> list[int]:
    hashMap = {}
    for i,n in enumerate(nums):
        if target - n in hashMap:
            return (hashMap[target-n], i)
        else:
            hashMap[n] = i
    return
# To test
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))