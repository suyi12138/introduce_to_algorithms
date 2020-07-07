# 7.1

class QuickSort:

    def __init__(self, nums: list):
        self.nums = nums

    def partition(self, q: int, r: int):
        x = self.nums[r]
        i = q - 1
        for j in range(q, r):
            if self.nums[j] <= x:
                i += 1
                self.nums[j], self.nums[i] = self.nums[i], self.nums[j]

        self.nums[r], self.nums[i+1] = self.nums[i+1], self.nums[r]
        return i+1

    def quick_sort(self, p, r):
        if p < r:
            q = self.partition(p, r)
            self.quick_sort(p, q-1)
            self.quick_sort(q+1, r)
