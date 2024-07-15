# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        main_list =[[1]]

        for _ in range(rowIndex):
            temp_list = [1]
            for i in range(len(main_list[-1])-1):
                if len(main_list[-1]) > 1:
                    temp_list.append(main_list[-1][i]+main_list[-1][i + 1])
            temp_list.append(1)
            main_list.append(temp_list)

        return main_list[-1]
    
print(Solution().getRow(0))