class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i:[] for i in range(numCourses)}

        for crs , pre in prerequisites:
            prevMap[crs].append(pre)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet: 
                return False           
            if prevMap[crs] == []: 
                return True
            
            visitSet.add(crs)
            for curr in prevMap[crs]:
                if not dfs(curr): 
                    return False
            visitSet.remove(crs)
            prevMap[curr] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True 

### Intuition
# To determine if all courses can be completed given their prerequisites, we can model the problem as a graph traversal problem where each course is a node and each prerequisite relationship is a directed edge. The problem then reduces to detecting a cycle in a directed graph, as the presence of a cycle would imply that it is impossible to complete all courses.

# ### Approach
# 1. **Graph Representation**:
#    - Represent the courses and their prerequisites as a graph using an adjacency list.
#    - Create a dictionary `prevMap` where each key is a course and the value is a list of prerequisites for that course.

# 2. **Depth-First Search (DFS)**:
#    - Use a set `visitSet` to keep track of the courses in the current DFS path to detect cycles.
#    - Define a helper function `dfs(crs)`:
#      - If the course is already in the `visitSet`, a cycle is detected, return `False`.
#      - If the course has no prerequisites (i.e., it is an empty list in `prevMap`), return `True`.
#      - Add the course to the `visitSet` and recursively visit all its prerequisites.
#      - If any prerequisite cannot be completed, return `False`.
#      - If all prerequisites are visited without finding a cycle, remove the course from the `visitSet`, mark its prerequisites as completed by setting `prevMap[crs]` to an empty list, and return `True`.

# 3. **Check All Courses**:
#    - Iterate through all courses and call the `dfs` function. If any course cannot be completed, return `False`.

# ### Time Complexity
# - **Time**: \(O(V + E)\), where \(V\) is the number of courses (vertices) and \(E\) is the number of prerequisite pairs (edges). Each course and prerequisite is processed once.

# ### Space Complexity
# - **Space**: \(O(V + E)\), for the adjacency list and the recursion stack during DFS.


               

