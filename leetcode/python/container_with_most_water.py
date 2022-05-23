#container with most water (leetcode)
# problem link - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, H: list[int]) -> int:
        ans, i, j = 0, 0, len(H)-1
        while (i < j):
            if H[i] <= H[j]:
                res = H[i] * (j - i)
                i += 1
            else:
                res = H[j] * (j - i)
                j -= 1
            if res > ans: ans = res
        return ans