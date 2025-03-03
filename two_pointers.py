from turtle import left, right
from typing import List


class two_pointers:

    # CONTAINER WITH MOST WATER
    # returns max area possible between two heights, from a given list of heights
    # Time complexity: O(n) (single loop through elements)
    # Space complexity: O(1) (no additional space required other than 2 pointers and result)
    def maxArea(self, heights: List[int]) -> int:
        # two pointers to point to the leftmost and rightmost ends
        left_pointer, right_pointer = 0, len(heights) - 1
        # initial result area is 0 before we iterate through list
        result = 0

        while left_pointer < right_pointer:
            # current area between the two pointers = 
            # minimum of current heights, into distance between those heights 
            area = (min(heights[left_pointer], heights[right_pointer]) 
                    * (right_pointer - left_pointer))
            # result area is to be updated to max of current area, or current result
            result = max(area, result)
            
            # the logic for below is that, the lower the pointer, the more it is to be moved
            # to get to a higher pointer, in order to maximize the area

            # if left pointer is lower than right pointer, move it more left 
            if (heights[left_pointer] <= heights[right_pointer]):
                left_pointer += 1
            # if right pointer is lower than left pointer, move it more right
            else:
                right_pointer -= 1
        
        return result
    
#######################################################################################

    # TRAPPING RAIN WATER
    # returns total rain water trapped between list of block heights
    # Time complexity: O(n) (one single loop through height list)
    # Space complexity: O(1) (only mem for pointers, maxes and result)
    def trapRainWater(self, height: List[int]) -> int:
        # if height array is null, return 0
        if not height:
            return 0
        
        # variable declaration
        left_pointer, right_pointer = 0, len(height) - 1
        left_max, right_max = height[left_pointer], height[right_pointer]
        result = 0

        # loop through array
        while left_pointer < right_pointer:
            # if left max is less than right max
            if left_max < right_max:
                # increase left pointer (move left)
                left_pointer += 1
                # set left max to the max of the current height, and the current left max
                left_max = max(left_max, height[left_pointer])
                # add to result the area trapped for this pointer
                # i.e., left max minus the current height
                result += left_max - height[left_pointer]
            # if right max is less than left max
            else:
                # decrease right pointer (move right)
                right_pointer -= 1
                # set right max to max of current height, and current right max
                right_max = max(right_max, height[right_pointer])
                # add to result the area trapped for this pointer
                # i.e., right max minus the current height
                result += right_max - height[right_pointer]
        return result