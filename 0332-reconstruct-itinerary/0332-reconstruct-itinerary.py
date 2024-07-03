class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src:[] for src, dst in tickets}

        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst) 

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res



# To solve the problem of finding an itinerary that uses all given flight tickets and starts from "JFK", we can use a Depth-First Search (DFS) approach. The goal is to construct an itinerary in lexicographical order whenever there are multiple valid solutions.

# ### Steps to Solve the Problem:

# 1. **Graph Construction**:
#    - Construct an adjacency list from the list of tickets, where each source airport points to a list of destination airports.
#    - Sort the adjacency lists so that we can use the smallest lexicographical order when exploring.

# 2. **Depth-First Search (DFS)**:
#    - Use DFS to explore all possible paths. Since we need to use all tickets exactly once, we should backtrack whenever we find that a path doesn't lead to a valid solution.
#    - Keep a result list initialized with the starting point "JFK".
#    - The DFS function will recursively visit nodes, append them to the result list, and remove used edges. If the current path fails to use all tickets, we backtrack by removing the last added node and reinserting the removed edge.

# 3. **Check Completion**:
#    - The recursion stops when the length of the result list equals the number of tickets plus one (indicating that all tickets are used exactly once).

# Here is the code implementation:

# ```python
# from collections import defaultdict

# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         adj = defaultdict(list)
        
#         # Sort tickets and populate the adjacency list
#         tickets.sort()
#         for src, dst in tickets:
#             adj[src].append(dst)

#         res = ["JFK"]

#         def dfs(src):
#             if len(res) == len(tickets) + 1:
#                 return True
#             if src not in adj:
#                 return False

#             temp = list(adj[src])  # Make a temporary copy of the adjacency list
#             for i, dst in enumerate(temp):
#                 adj[src].pop(i)
#                 res.append(dst)
#                 if dfs(dst):
#                     return True
#                 adj[src].insert(i, dst)
#                 res.pop()
#             return False

#         dfs("JFK")
#         return res
# ```

# ### Explanation:

# 1. **Graph Construction**:
#    - We use `defaultdict(list)` to construct the adjacency list.
#    - `tickets.sort()` ensures that we always consider the smallest lexicographical order first when multiple destinations are possible.

# 2. **DFS with Backtracking**:
#    - We start DFS from "JFK".
#    - For each node, we explore all possible destinations by iterating through its adjacency list.
#    - We temporarily remove the edge being used and recursively continue the DFS. If a valid itinerary is found (`len(res) == len(tickets) + 1`), we return `True`.
#    - If a path is invalid, we backtrack by removing the last node from `res` and reinserting the edge back into the adjacency list.

# 3. **Edge Case**:
#    - The implementation assumes there is always at least one valid itinerary. The problem guarantees that there is one, given the problem constraints.

# This approach ensures we explore all possible paths in lexicographical order, and by using backtracking, we can efficiently find the correct itinerary.





            