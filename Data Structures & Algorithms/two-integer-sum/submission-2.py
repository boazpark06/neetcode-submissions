class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary.
        # It will store each number as the key 
        # and that number's index as the value.
        #
        # Example:
        # nums = [2, 7, 11]
        # myHash = {2: 0, 7: 1, 11: 2}
        myHash = {}

        # Go through every number in nums.
        # i = index of the number
        # n = actual number
        for i, n in enumerate(nums):
            # Store the number and where it appears in the list.
            myHash[n] = i

        # Go through the list again to find the two numbers.
        for i, n in enumerate(nums):

            # Figure out what number we need to add to n
            # to reach the target.
            #
            # Example:
            # target = 9
            # n = 2
            # diff = 9 - 2 = 7
            diff = target - n

            # Check if the number we need exists in the dictionary.
            #
            # Also make sure we are not using the same list element twice.
            if diff in myHash and myHash[diff] != i:

                # Return the index of the current number
                # and the index of the other number.
                return [i, myHash[diff]]
                    

        