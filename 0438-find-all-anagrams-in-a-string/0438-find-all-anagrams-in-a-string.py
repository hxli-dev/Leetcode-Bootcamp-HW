from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []

        def idx(c):  
            return ord(c) - ord('a')

        need = [0] * 26
        for ch in p:
            need[idx(ch)] += 1

        res = []
        win = [0] * 26
        left = 0

        for right in range(n):
            win[idx(s[right])] += 1

          
            if right - left + 1 > m:
                win[idx(s[left])] -= 1
                left += 1

           
            if right - left + 1 == m and win == need:
                res.append(left)

        return res
