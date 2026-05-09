class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # res = [0] * len(arr)
        # res[-1] = -1
        # m = -1

        # for i in range(len(arr)-2, -1, -1):
        #     m = max(m, arr[i+1])
        #     res[i] = m
        
        # return res

        m = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            m = max(m, arr[i+1])
            temp = max(m, arr[i])
            arr[i] = m
            m = temp
        
        arr[-1] = -1
        return arr