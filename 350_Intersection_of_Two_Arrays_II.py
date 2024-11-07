# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

class Solution_1:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        iter = []
        array_search = []
        result = []
        index_array_serach = []
        if len(nums1) > len(nums2):
            iter = nums1
            array_search = nums2
        else:
            iter = nums2
            array_search = nums1

        for i in range(len(array_search)):
            for j in range(len(iter)): 
                if array_search[i] == iter[j] and j not in index_array_serach:
                    result.append(array_search[i])
                    index_array_serach.append(j)
                    break                    
                    
        return result 

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hash_map = {}
        result = []
        for i in range(len(nums1)):
            if nums1[i] in hash_map:
                hash_map[nums1[i]]+=1
            else:
                hash_map[nums1[i]] = 1
        
        for i in range(len(nums2)):
            if nums2[i] in hash_map and hash_map[nums2[i]] > 0:
                result.append(nums2[i])
                hash_map[nums2[i]]-=1
        return result
          







