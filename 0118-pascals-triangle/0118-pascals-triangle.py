class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            temp = [0]+ res[-1] +[0]
            row = []
            for j in range(len(res[-1]) +1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res


# Intuition and Approach:

# - We're generating Pascal's Triangle up to a given number of rows `numRows`.
# - We start with the first row containing just one element, which is 1.
# - Then, for each subsequent row, we create it based on the previous row.
# - For each row, we add a 0 to the beginning and end of the previous row to help calculate the values for the current row.
# - We iterate through each pair of adjacent elements in the previous row, sum them, and append the sums to form the new row.
# - Finally, we append each new row to the result list.

# Time Complexity: O(numRows^2) - Each row requires calculation of elements proportional to its row number. So the time complexity is quadratic.

# Space Complexity: O(numRows^2) - The space needed to store the entire Pascal's Triangle up to `numRows`. Each row has row number elements, and there are `numRows` rows. Therefore, the space complexity is quadratic as well.
