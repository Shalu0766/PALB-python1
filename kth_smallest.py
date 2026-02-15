class Solution:
    def kthSmallest(self, arr, k):
        low = min(arr)
        high = max(arr)

        while low < high:
            mid = (low + high) // 2

            count = 0
            for num in arr:
                if num <= mid:
                    count += 1

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low
