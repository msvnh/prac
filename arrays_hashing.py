from collections import defaultdict
from typing import DefaultDict, List

class arrays_hashing:

    # CONTAINS DUPLICATE
    # Checks if a list of numbers has a duplicate entry
    # Time complexity: O(n) (single loop through list of ints)
    # Space complexity: O(n) (one set, max which can go till number of ints)
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = {}
        for num in nums:
            if num in seen_set:
                return True
            seen_set.add(num)
        return False
    
##################################################################################################

    # VALID ANAGRAM
    # Checks if two strings are valid anagrams (same letters possibly rearranged)
    # Time complexity: O(n) (n being size of strings, single loop through string)
    # Space complexity: O(n) (2 sets based on length of string)
    def isAnagram(self, s: str, t: str) -> bool:
        # inital length check
        if (len(s) != len(t)):
            return False
        
        # create 2 sets to store char count
        letter_count_s, letter_count_t = {}, {}

        # loop through strings, adding count of chars in both sets
        for i in range(len(s)):
            letter_count_s[s[i]] = 1 + letter_count_s.get(s[i], 0)
            letter_count_t[t[i]] = 1 + letter_count_t.get(t[i], 0)

        # check and return if both the sets are equal
        return letter_count_s == letter_count_t
    
##################################################################################################

    # TWO SUM
    # checks if there exist 2 numbers in a list, that can add up to the target
    # Time complexity: O(n) (single loop through list of ints)
    # Space complexity: O(n) (one hashmap to store list of ints for difference)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap to store values and their corresponding indices
        hashmap = {}

        # iterate through the number list
        for i, n in enumerate(nums):
            diff = target - n
            # if the diff is present in hashmap,
            # it's index would be lower than the current index
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i

        #return empty array in case sum is not possible
        return []
    
##################################################################################################
    
    # GROUP ANAGRAMS
    # from a list of strings, group anagrams
    # Time complexity: O(n*m) (loop through list of strings, and individual string chars once)
    # Space complexity: O(n) (one dictionary, to store strings, and worst case, all would be different strings (no anagrams))
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a defaultdict object of lists.
        # why defaultdict? because it will initialize a new list object
        # in case we try to access a pair where the key is not preset
        result = defaultdict(list)

        # loop through strings and create and array of 26 0's
        # this array will indicate the char count (letters only) of the current string
        for string in strs:
            count = [0] * 26

            # for each char in the string, add 1 to it's existing count
            # since the array is initialized with 0, no need to worry about defaults
            for char in string:
                count[ord(char)-ord('a')] += 1
            
            # this unique array of char counts will be our key for the dict
            # add the current string to this key (append because it is a list)
            result[tuple(count)].append(string)

        # return the values as a list as per requirement
        return list(result.values())
    
##################################################################################################

    # VALID SUDOKU
    # checks if a sudoku board is valid or not (only valid, not if solvable)
    # Time complexity: O(9^2) (since it is being looped over 81 times)
    # Space complexity: O(9^2) (since )
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # one set per column to check for uniqueness of column
        cols = defaultdict(set)
        
        # one set per row to check for uniqueness of row
        rows = defaultdict(set)

        # one set per square (row/3, column/3) is the index of square (0,0) or (2,1), etc.
        squares = defaultdict(set)

        # loop through 9 rows and 9 columns
        for r in range(9):
            for c in range(9):
                # assign a variable for easier access of board element
                elem = board[r][c]
                # continue if empty
                if elem == ".":
                    continue
                # check if element already in a row, col or square
                # if yes, invalid, hence return false.
                if (elem in cols[c] or
                    elem in rows[r] or
                    elem in squares[(r//3,c//3)]):
                    return False
                
                # add element to rows, cols and squares set and continue loop
                cols[c].add(elem)
                rows[r].add(elem)
                squares[(r//3,c//3)].add(elem)
        return True;