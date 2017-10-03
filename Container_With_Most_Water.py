Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


# FINDING THE AREA USING A QUICK sort

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        curr_area = 0
        start = 0
        finish = len(height) - 1

        while start != finish:
            curr_area = min(height[start],height[finish]) * (finish-start)
            if curr_area > max_area:
                max_area = curr_area
            if height[start] < height[finish]:
                start += 1
            else:
                finish -= 1
        return max_area
