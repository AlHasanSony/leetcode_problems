#problem link - https://leetcode.com/problems/reshape-the-matrix/


from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        ret = []
        for i in range(m):
            for j in range(n):
                if (i * n + j) % c == 0:
                    ret.append([])
                ret[-1].append(nums[i][j])

        return ret 











# class Solution(object):
#     def matrixReshape(self, mat, r, c):

#         m, n = len(mat), len(mat[0])
#         if m * n != r * c:
#             return mat
#         ans = [[0 for _ in range(c)] for _ in range(r)]
#         p1, p2 = 0, 0
#         for i in range(m):
#             for j in range(n):
#                 ans[p1][p2] = mat[i][j]
#                 p2 += 1
#                 if p2 == c:
#                     p1 += 1
#                     p2 = 0
#         return ans