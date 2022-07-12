#75. Sort Colors
# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo = 0
        hi = len(a) - 1
        mid = 0
        while mid <= hi:
            if a[mid] == 0:
                a[lo], a[mid] = a[mid], a[lo]
                lo = lo + 1
                mid = mid + 1
            elif a[mid] == 1:
                mid = mid + 1
            else:
                a[mid], a[hi] = a[hi], a[mid] 
                hi = hi - 1
        return a
        
