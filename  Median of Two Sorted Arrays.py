There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
Subscribe to see which companies asked this question.

Show Tags


def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """



class Solution(object):

    arr1 = [1,2,2,3]
    arr2 = [-5,2,3,4,5]
    arr3 = [-5,1,2,2,2,3,3,4,5]

    i1 = 0
    i2 = 0
    arr3 = []
    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1] < arr2[i2]:
            arr3.append(arr1[i1])
            i1 += 1
        else:
            arr3.append(arr2[i2])
            i2 += 1
    if i1 == len(arr1):
        while i2 < len(arr2):
            arr3.append(arr2[i2])
            i2 += 1
    if i2 == len(arr2):
        while i1 < len(arr1):
            arr3.append(arr1[i1])
            i1 += 1

    count = len(arr3)
    #not zero == true
    if count % 2:
        return arr3[count/2]
    else:
        return (0. + arr3[count/2] + arr3[count/2 - 1])/2
