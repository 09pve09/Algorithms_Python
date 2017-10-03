Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"]


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        results = {}
        for string in sorted(strs):
            sorted_string = ''.join(sorted(string))
            results[sorted_string] = results.get(sorted_string,[]) + [string]
        return results.values()
