Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_str = ""
        start = 0
        if not strs:
            return longest_str
        else:
            for i in range(0, len(strs[start])):
                end = len(strs) - 1
                while start != end:
                    if i > len(strs[end])-1 or strs[start][i] != strs[end][i]:
                        return longest_str
                    elif strs[start][i] == strs[end][i]:
                        end -= 1
                if start == end:
                    longest_str = longest_str + strs[start][i]
            return longest_str
