Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Subscribe to see which companies asked this question.

Show Tags
Show Similar Problems


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in xrange(len(nums)-2):
            left = i+1
            right = len(nums) - 1
            while left < right:
                sum_of_nums = nums[i] + nums[left] + nums[right]
                if sum_of_nums == target:
                    return sum_of_nums
                if abs(sum_of_nums - target) < abs(result - target):
                    result = sum_of_nums
                if sum_of_nums < target:
                    left += 1
                elif sum_of_nums > target:
                    right -= 1
        return result
