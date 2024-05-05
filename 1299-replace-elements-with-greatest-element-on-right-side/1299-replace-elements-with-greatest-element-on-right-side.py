class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax 
            rightMax = newMax
        return arr


# Intuition and Approach:

# - We're given an array `arr`.
# - For each element in `arr`, we want to replace it with the maximum element to its right, and for the last element, we replace it with -1.
# - We initialize `rightMax` to -1 to keep track of the maximum element seen so far.
# - We iterate through `arr` in reverse order, starting from the second-to-last element.
# - For each element at index `i`, we find the maximum between `rightMax` and `arr[i]`. This represents the maximum element to the right of `arr[i]`.
# - We update `arr[i]` with the current value of `rightMax`, as it represents the maximum element to the right of `arr[i]`.
# - We update `rightMax` with the new maximum value (`newMax`) found in the current iteration.
# - Finally, we return `arr` with the elements replaced.

# Time Complexity: O(n) - where n is the length of `arr`. We iterate through `arr` once.

# Space Complexity: O(1) - We use only a constant amount of extra space for variables (`rightMax` and `newMax`) regardless of the size of `arr`.
