class Solution:
    def rotate(self, arr):
        n = len(arr)

        prev = arr[n - 1]   # last element

        for i in range(n):
            arr[i], prev = prev, arr[i]

        return arr
