class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [nums for nums,_ in count.most_common(k)]


# Intuition and Approach:

# - We're given a list of integers `nums` and an integer `k`.
# - We want to return the `k` most frequent elements in `nums`.
# - We use the Counter class from the collections module to count the occurrences of each element in `nums`.
# - The `most_common(k)` method of Counter returns a list of tuples containing the `k` most common elements and their counts, sorted in descending order.
# - We use a list comprehension to extract just the elements (keys) from these tuples and return them.

# Time Complexity: O(n log k), where n is the number of elements in `nums`. Counting the occurrences of each element takes linear time, and finding the `k` most common elements takes O(n log k) time due to sorting.

# Space Complexity: O(n), where n is the number of elements in `nums`. The space used by the Counter object and the list returned has a linear relationship with the size of `nums`.
