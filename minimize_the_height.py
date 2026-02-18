class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        
        arr.sort()
        ans = arr[-1] - arr[0]
        small = arr[0] + k
        large = arr[-1] - k
        if small > large:
            small, large = large, small
        
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            
            minimum = min(small, arr[i] - k)
            maximum = max(large, arr[i - 1] + k)
            
            ans = min(ans, maximum - minimum)
        
        return ans
