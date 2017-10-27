# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0


#My solution
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        min, max = 0, len(nums)-1
        while min < max:
            print 'inside while'
            mid = (min+max)/2
            print 'mid:', mid
            if target < nums[mid]:
                max = mid - 1
            elif target > nums[mid]:
                min = mid + 1
            else:
                return mid
        if target <= nums[min]:
            return min
        else:
            return min+1
