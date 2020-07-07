# 8.2

class CountingSort:

    def __init__(self, nums: list, max: int):
        # 待排序数组， 每个元素都是0到k区间内的一个整数
        self.nums = nums
        # 待排序数组中元素的最大可能值
        self.max = max
        # 待排序数组的长度
        self.length = len(nums)

    def counting_sort(self):
        c = [0 for _ in range(self.max+1)]
        b = [0 for _ in range(self.length)]
        print(b)
        for j in range(self.length):
            c[self.nums[j]] += 1
        for i in range(1, self.max+1):
            c[i] += c[i-1]
        print(c)
        for j in range(self.length-1, -1, -1):
            b[c[self.nums[j]]-1] = self.nums[j]
            c[self.nums[j]] -= 1
        return b