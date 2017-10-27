
# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return [-1,-1]
        min, max = 0, len(nums)-1;
        while min <= max:
            mid = (min+max)/2
            if target > nums[mid]:
                min = mid+1
            elif target < nums[mid]:
                max = mid-1
            else:
                # print 'found target at index: ', mid
                break
        # print 'looking for a range'
        if nums[mid] != target:
            return [-1,-1]
        else:
            left = right = mid
            left_stop = right_stop = True
            while left_stop or right_stop:
                # print 'searching...'
                if left-1 >= 0 and nums[left-1] == nums[mid]:
                    left = left - 1
                else:
                    left_stop = False
                if right+1 < len(nums) and nums[right+1] == nums[mid]:
                    right = right+1
                else:
                    right_stop = False
            return [left, right]
