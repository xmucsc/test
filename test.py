'''Classical Binary Search
https://www.lintcode.com/problem/classical-binary-search/description
'''

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
