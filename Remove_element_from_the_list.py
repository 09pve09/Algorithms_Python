# Given an array and a value, remove all instances of that value in place and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
# Given input array nums = [3,2,2,3], val = 3
#
# Your function should return length = 2, with the first two elements of nums being 2.

# My Solution
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        count = 0
        while i < len(nums)-count:
            # print 'i:', i
            # print 'count:', count
            if nums[i] == val:
                # print 'match found'
                for j in range(i, len(nums)-count):
                    try:
                        nums[j], nums[j+1] = nums[j+1], nums[j]
                        # print 'swapped', nums
                    except:
                        pass
                count += 1
                # print 'count apdated:',count
            else:
                i += 1
        # print count
        if count != 0:
            nums = nums[:-count]
        return len(nums)
