# 7.1
import random

class QuickSort:

    def __init__(self, nums: list):
        self.nums = nums

    def partition(self, p: int, r: int):
        x = self.nums[r]
        i = p - 1
        for j in range(p, r):
            if self.nums[j] <= x:
                i += 1
                self.nums[j], self.nums[i] = self.nums[i], self.nums[j]

        self.nums[r], self.nums[i+1] = self.nums[i+1], self.nums[r]
        return i+1

    def randomized_partition(self, p: int, r: int):
        i = random.randint(p, r)
        self.nums[i], self.nums[r] = self.nums[r], self.nums[i]
        return self.partition(p, r)

    def quick_sort(self, p: int, r: int):
        if p < r:
            q = self.partition(p, r)
            self.quick_sort(p, q-1)
            self.quick_sort(q+1, r)

    def randomized_quick_sort(self, p: int, r: int):
        if p < r:
            q = self.randomized_partition(p, r)
            self.randomized_quick_sort(p, q-1)
            self.randomized_quick_sort(q+1, r)