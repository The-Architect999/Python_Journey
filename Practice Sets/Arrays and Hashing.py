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
# Anagram
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


# ======================================================================================
# •	Two Sum
# ======================================================================================
#Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target. 
# Assume exactly one valid answer exists, and you may not use the same element twice.
# Example 1:
nums = [2, 7, 11, 15]
target = 9
# Output: [0, 1]  (2 + 7 = 9)
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = set()
    for i, no in enumerate(nums):
        need = target - no
        if need in seen:
            return [nums.index(need), i]
        seen.add(no)

# here i remember that it is always beter to find in set as the items are basically the index and hence 0(1) complexity so chose set
# the time complexity here if i understand it correctly is O(n) as there's a loop that iterates once, and theres a list indexing that runs exactly once
# so that's 0(n) but because the indexing runs exactly once, its O(n+n) which is O(n)
print(two_sum(nums, target))

'''ERROR'''
# if there were multiple close matches or this ran inside another loop, that .index() cost multiplies. 
# More importantly for a real OA: .index() also has a subtle correctness risk — if a value appears more than once in nums,
# .index() always returns the first occurrence, which might not be the one your seen set was even referring to.
'''FIX: REPLACE SET with DICT'''

def two_sum(nums: list[int], target: int) -> list[int]:
    seen = dict()
    for i, no in enumerate(nums):
        need = target - no
        if need in seen:
            return [seen[need], i]
        seen[no] = i

print(two_sum(nums, target))


# ======================================================================================
# •	Group Anagrams
# ======================================================================================
# Given an array of strings strs, group the anagrams together. You can return the groups in any order.
# Example:
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# # Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
# def group_anagrams(strs: list[str]) -> list[list[str]]:

#     seen = {}
#     for words in strs:
#         seen[words] = {}
#         for letters in words:
#             if letters in seen[words]:
#                 seen[words][letters] += 1
#             else:
#                 seen[words][letters] = 1
#     # {'eat': {'e': 1, 'a': 1, 't': 1}, 'tea': {'t': 1, 'e': 1, 'a': 1}, 
#     #  'tan': {'t': 1, 'a': 1, 'n': 1}, 'ate': {'a': 1, 't': 1, 'e': 1}, 'nat': {'n': 1, 'a': 1, 't': 1}, 'bat': {'b': 1, 'a': 1, 't': 1}}
#     counter = len(strs)
#     temp = []
#     for items in strs:
#         if seen[items] == 

# print(group_anagrams(strs))


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagrams(strs):
    groups = {}  # key -> list of words
    for word in strs:
        key = ''.join(sorted(word)) # this is now hashable
        if key not in groups:   # if key not in groups, create empty list first
            groups[key] = []
            
        if key in groups: # then append word to groups[key]
            groups[key].append(word)

    return list(groups.values())

print(group_anagrams(strs))

'''
this one was tough to crack, documentation pending
'''
















