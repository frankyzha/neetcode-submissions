class Solution:
    def calPoints(self, operations: List[str]) -> int:
        nums = []
        for i in operations:
            if i == '+':
                nums.append(nums[-1] + nums[-2])
            elif i == 'D':
                nums.append(nums[-1] * 2)
            elif i == 'C':
                nums.pop()
            else:
                nums.append(int(i))
        
        return sum(nums)