'''
Given a sorted array of distinct integers and a target value, return the index if
the target is found. If not, return the index where it would be
if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ind = 0
        current = nums[0]
        for index, value in enumerate(nums):
            if value >= target and value > current:
                return index
        return len(nums)