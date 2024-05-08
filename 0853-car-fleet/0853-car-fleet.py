class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        stack = []

        for p,s in sorted(pair)[::-1]:
            stack.append((target - p)/ s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
 


# Intuition:
# - We have cars at different positions and speeds, and we want to determine how many car fleets will arrive at the target destination at the same time.
# - Car fleets form when cars reach the target destination at the same time or when they catch up with the car in front of them.

# Approach:
# - We first create pairs of position and speed for each car.
# - We sort these pairs based on positions in descending order.
# - We use a stack to track the time it takes for each car to reach the target, calculated as `(target - position) / speed`.
# - While iterating through the sorted pairs, we calculate the time for each car to reach the target and push it onto the stack.
# - If the time for the current car is less than or equal to the time for the car on top of the stack, it means they form a fleet, so we pop the stack.
# - We continue this process until all cars are processed.
# - The number of cars left in the stack represents the number of car fleets.

# Time Complexity: O(n log n) - Sorting the pairs of position and speed takes O(n log n) time, where n is the number of cars.

# Space Complexity: O(n) - The stack can potentially store all the cars. In the worst-case scenario, all cars form individual fleets, so the space complexity is O(n).