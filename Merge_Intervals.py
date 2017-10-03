Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 1:
            return []
        sorted_intervals = sorted(intervals, key=lambda x:x.start)
        results = [sorted_intervals[0]]
        for next_interval in sorted_intervals[1:]:
            if next_interval.start <= results[-1].end:
                results[-1].end = max( results[-1].end, next_interval.end )
            else:
                results.append(next_interval)
        return results

        
