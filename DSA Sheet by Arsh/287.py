#287. Find the Duplicate Number
#https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = [0 for i in range(len(nums) + 1)]
        for num in nums:
            count[num] += 1
            if count[num] > 1:
                return num
