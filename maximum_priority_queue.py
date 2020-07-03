# 6.5
from heap import Heap

class MaximumPriorityQueue:
    def __init__(self, nums):
        self.heap_instance = Heap(nums)
        self.heap_instance.build_max_heap()
        self.heap_instance.heap_length = self.heap_instance.nums_length

    def maximum(self):
        return self.heap_instance.nums[0]

    def extract_max(self):
        if self.heap_instance.heap_length <= 1:
            print("heap underflow")
            return None
        max = self.heap_instance.nums[0]
        self.heap_instance.nums[0], self.heap_instance.nums[self.heap_instance.heap_length-1] = self.heap_instance.nums[self.heap_instance.heap_length-1], self.heap_instance.nums[0]
        self.heap_instance.heap_length -= 1
        self.heap_instance.max_heapify(0)
        return max

    def increase_key(self, index: int, key):
        if key < self.heap_instance.nums[index]:
            print("new key is smaller than current key")
            return None

        self.heap_instance.nums[index] = key
        while index > 0 and self.heap_instance.nums[self.heap_instance.parent(index)] < self.heap_instance.nums[index]:
            self.heap_instance.nums[index], self.heap_instance.nums[self.heap_instance.parent(index)] = self.heap_instance.nums[self.heap_instance.parent(index)], self.heap_instance.nums[index]
            index = self.heap_instance.parent(index)

    def insert(self, key):
        self.heap_instance.heap_length += 1
        self.heap_instance.nums_length += 1
        if self.heap_instance.heap_length == self.heap_instance.nums_length:
            self.heap_instance.nums.append(float('-inf'))
        else:
            self.heap_instance.nums[self.heap_instance.heap_length - 1] = float('-inf')
        self.increase_key(self.heap_instance.heap_length-1, key)
