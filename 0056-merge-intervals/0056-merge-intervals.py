class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nlogn)
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for first, end in intervals[1:]:
            lastEnd = output[-1][1]

            if first <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([first, end])

        return output
