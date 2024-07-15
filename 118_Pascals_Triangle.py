# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        main_list =[[1]]

        for _ in range(numRows-1):
            temp_list = [1]
            for i in range(len(main_list[-1])-1):
                if len(main_list[-1]) > 1:
                    temp_list.append(main_list[-1][i]+main_list[-1][i + 1])
            temp_list.append(1)
            main_list.append(temp_list)

        return main_list 