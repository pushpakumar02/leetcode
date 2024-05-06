class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        return clean_s == clean_s[::-1]     

# Intuition and Approach:

# - The task is to determine whether a given string `s` is a palindrome, considering only alphanumeric characters and ignoring cases.
# - We first create a cleaned version of the string `s` containing only alphanumeric characters and converted to lowercase.
# - To create the cleaned string:
#   - We iterate through each character `char` in `s`.
#   - If `char` is alphanumeric (checked using `char.isalnum()`), we add it to the cleaned string after converting it to lowercase (`char.lower()`).
# - After cleaning, we check if the cleaned string is equal to its reverse. If it is, then `s` is a palindrome.
# - We use slicing (`clean_s[::-1]`) to reverse the cleaned string and compare it with the original cleaned string.

# Time Complexity: O(n) - where n is the length of the input string `s`. Creating the cleaned string requires iterating through each character once, and comparing it with its reverse takes linear time.

# Space Complexity: O(n) - We create a cleaned version of the string `s`, which takes space proportional to the length of `s`. Additionally, we have the space complexity of the reversed string, which also takes space proportional to the length of `s`. Therefore, the overall space complexity is linear.
