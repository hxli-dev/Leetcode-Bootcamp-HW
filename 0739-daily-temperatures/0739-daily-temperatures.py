from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n          # 默认都是 0（如果后面没更热的就保持 0）
        stack = []             # 存下标，保证栈里的温度是递减的

        for i, t in enumerate(temperatures):
            # 只要今天比栈顶那天热，就结算栈顶那天
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()       # j 这天等来了更暖的一天 i
                ans[j] = i - j
            # 今天这天压入栈，等将来遇到比它更暖的
            stack.append(i)

        return ans
