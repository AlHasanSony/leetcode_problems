#problem -  https://leetcode.com/problems/reverse-bits/


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n: int) -> int:
        num = 0
        for i in range(32):
            if (n >> i) & 1:
                num += ((n >> i) & 1) << (31 - i)
        return num