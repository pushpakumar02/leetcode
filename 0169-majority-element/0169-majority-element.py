class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return count.most_common(1)[0][0]

# Intuition and Approach:

# - The problem is to find the majority element in an array, i.e., the element that appears more than ⌊n / 2⌋ times, where n is the length of the array.
# - We can use the Counter class from the collections module to count the occurrences of each element in the array.
# - After counting, we can return the most common element using the `most_common()` method of Counter.
# - The most common element is returned as a list of tuples, where each tuple contains the element and its count.
# - Since we are looking for the majority element, we take the first element of the first tuple from the list returned by `most_common()`.

# Time Complexity: O(n) - where n is the length of the array `nums`. Counting the occurrences of each element takes linear time.

# Space Complexity: O(n) - The Counter object requires additional space proportional to the number of unique elements in `nums`. Additionally, we have a constant amount of space used for other variables.
