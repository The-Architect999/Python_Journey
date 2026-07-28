# ======================================================================================
# contains duplicates
# ======================================================================================

# Given an integer array nums, return True if any value appears at least twice in the array, and False if every element is distinct.
# Example 1:
nums = [1, 2, 3, 1]
# Output: True

# Example 2:
# nums = [1, 2, 3, 4]
# Output: False

# Example 3:
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: True
def contains_duplicate(nums: list[int]) -> bool:
    found = set()
    for num in nums:
        if num in found:
            return True
        found.add(num)
    return False
#complexity O(n)
print(contains_duplicate(nums))
# Constraint: aim for O(n) — think about what data structure lets you check 
# "have I seen this before?" in O(1) per lookup, same idea as seen from the sliding window problem.
'''
used set to make use of hashing
'''

# ======================================================================================
# contains duplicates
# ======================================================================================
#Given two strings s and t, return True if t is an anagram of s (same letters, same counts, any order), False otherwise.
# Aim for O(n) again — same "have I seen this before, how many times" idea, just counting instead of a plain set.
def is_anagram(s: str, t: str) -> bool:
    seen = dict()
    if len(t) != len(s):
        return False
    for letter in t:
        if letter not in seen:
            seen[letter] = 1
        else:
            seen[letter] += 1
    for letter in s:
        if letter in seen:
            seen[letter] -= 1
        else:
            return False
        
    for v in seen.values():  # made a mistake here, added all the values in the dict so -1, +1 cancelled each other and the sum still returned 0
        if v != 0:          # fixed it by checking if evey value == 0.
            return False
    return True

# it has 3 iterations but is still not O(n²)
# this is O(n+m+c) which is still O(n) hence meets the constraints
print(is_anagram("anagram", "nagaram"))
