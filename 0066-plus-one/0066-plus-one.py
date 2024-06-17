class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else:
                digits.append(1)
                one = 0
            i += 1
        return digits[::-1]


### Intuition

# To add one to an integer represented as an array of digits, we need to handle the addition and carry-over operations manually, much like how you would do addition by hand.

# ### Approach

# 1. **Reverse the List**: Reversing the list makes it easier to handle the addition from the least significant digit (the end of the number) to the most significant digit (the start of the number).
# 2. **Initialize Carry**: Start with a carry of 1 (since we are adding one to the number).
# 3. **Iterate and Add**:
#    - Traverse through the reversed list.
#    - Add the carry to the current digit.
#    - If the resulting digit is 10, set it to 0 and keep the carry as 1.
#    - Otherwise, set the digit to the new value and set the carry to 0.
# 4. **Handle Extra Carry**: If after processing all digits the carry is still 1, append a new digit 1 to the list.
# 5. **Reverse Back**: Finally, reverse the list back to its original order and return it.

# ### Steps

# 1. Reverse the input list `digits`.
# 2. Initialize `one` (carry) to 1 and `i` (index) to 0.
# 3. Use a while loop to iterate through the list and handle the addition:
#    - If `i` is within the bounds of `digits`, check the current digit:
#      - If it's 9, set it to 0 (since 9 + 1 = 10, carry the 1).
#      - Otherwise, add 1 to the digit, set `one` to 0 (since no further carry is needed), and break the loop.
#    - If `i` is out of bounds, append 1 to the list (since we need to extend the number by one more digit).
# 4. Reverse the list back and return it.

# ### Time and Space Complexities

# - **Time Complexity**: O(n), where n is the number of digits. Each digit is processed once.
# - **Space Complexity**: O(1) extra space, ignoring the input and output space.

# ### Implementation

# ```python
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         digits = digits[::-1]
#         one, i = 1, 0

#         while one:
#             if i < len(digits):
#                 if digits[i] == 9:
#                     digits[i] = 0
#                 else:
#                     digits[i] += 1
#                     one = 0
#             else:
#                 digits.append(1)
#                 one = 0
#             i += 1
#         return digits[::-1]
# ```

# ### Explanation

# 1. **Reverse the Digits**: We reverse the digits so that we start processing from the least significant digit.
# 2. **Carry Initialization**: We start with a carry (`one`) of 1 since we are adding one to the number.
# 3. **Iteration with Carry Handling**:
#    - Traverse through the digits.
#    - If the current digit is 9, set it to 0 and continue with the carry.
#    - If the current digit is less than 9, increment it by 1, set the carry to 0, and exit the loop.
#    - If all digits are processed and we still have a carry, append a 1 to the list.
# 4. **Final Reverse**: Reverse the list back to its original order.

# This solution effectively handles the addition operation with proper carry management and ensures that the number is correctly incremented by one.