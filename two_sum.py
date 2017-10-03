Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
Subscribe to see which companies asked this question.

Show Tags
Show Similar Problems

# O(n^2) solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = 0
        list = []
        while ( count < len(nums)):
            first_input = nums[count]
            target_input = target - first_input
            for idx, val in enumerate(nums):
                if idx != count and val == target_input:
                    list.append(count)
                    list.append(idx)
                    return list
                else:
                    continue
            count += 1

# O(n) solution(MUCH BETTER)

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            #looking for a match among the differences stored in a dict
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]

            else:
                #storing the difference after didaction as a key and idex of the didactud number as a value
                buff_dict[target - nums[i]] = i
