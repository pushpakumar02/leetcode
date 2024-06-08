class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prevMap = {i: [] for i in range(numCourses)}

        for i, pre in prerequisites:
            prevMap[i].append(pre)

        output = []
        path, visit = set(), set()
        def dfs(c):
            if c in path:
                return False
            if c in visit:
                return True
            
            path.add(c)
            for pre in prevMap[c]:
                if dfs(pre) == False:
                    return False
            path.remove(c)
            visit.add(c)
            output.append(c)
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

### Intuition
# To determine the order in which courses should be taken given their prerequisites, we can use a graph traversal approach similar to topological sorting. This ensures that we respect the prerequisite relationships between courses.

# ### Approach
# 1. **Graph Representation**:
#    - Represent the courses and their prerequisites using an adjacency list.
#    - Create a dictionary `prevMap` where each key is a course and the value is a list of prerequisites for that course.

# 2. **DFS for Topological Sort**:
#    - Use two sets: `visit` to keep track of all courses that have been completely processed and `path` to keep track of the current recursion stack to detect cycles.
#    - Define a helper function `dfs(c)`:
#      - If the course is in `path`, a cycle is detected, so return `False`.
#      - If the course is in `visit`, it has already been processed, so return `True`.
#      - Add the course to `path` and recursively visit all its prerequisites.
#      - If any prerequisite causes a cycle, return `False`.
#      - Once all prerequisites are processed without detecting a cycle, remove the course from `path`, mark it as visited by adding it to `visit`, and add it to the `output` list.
   
# 3. **Check All Courses**:
#    - Iterate through all courses and call the `dfs` function. If any course results in a cycle, return an empty list.
#    - Reverse the `output` list to get the correct order of courses.

# ### Time Complexity
# - **Time**: \(O(V + E)\), where \(V\) is the number of courses (vertices) and \(E\) is the number of prerequisite pairs (edges). Each course and prerequisite is processed once.

# ### Space Complexity
# - **Space**: \(O(V + E)\), for the adjacency list and the recursion stack during DFS.