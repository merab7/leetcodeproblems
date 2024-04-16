""" 
One-pass Hash Table
Algorithm

It turns out we can do it in one-pass. While we are iterating and inserting elements 
into the hash table, we also look back to check if current element's complement already 
exists in the hash table. If it exists, we have found a solution and return the indices immediately.

Implementation


Complexity Analysis

Time complexity: O(n)O(n)O(n).
We traverse the list containing nnn elements only once. Each lookup in the table costs only O(1)O(1)O(1) time.

Space complexity: O(n)O(n)O(n).
The extra space required depends on the number of items stored in the hash table, which stores at most nnn elements.
""" 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


"""Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left."""       

class Solution:
    def isPalindrome(self, x: int) -> bool:
        matrix = []
        for y in str(x):
            matrix.insert(0, y)
        return "".join(matrix) == str(x)
 