Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        result = ""
        max_length = 0
        for i in range(len(s)):
            if s[i] not in result:
                result = result + s[i]
            else:
                result = result[result.index(s[i])+1:] + s[i]
            if max_length < len(result):
                max_length = len(result)
        return max_length

        
