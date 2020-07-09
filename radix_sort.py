# 8.3


class RadixSort:

    def __init__(self, nums: list, d: int, k: int):
        # 待排序数组
        self.nums = nums
        # 待排序数组中的每个元素的位数
        self.d = d
        # 待排序数组中每个元素每一位可能取值个数
        self.k = k

    def radix_sort(self):
        for i in range(self.d-1, -1, -1):
            c = [0 for _ in range(self.k+1)]
            b = [0 for _ in range(len(self.nums))]
            tmp_nums = [int(str(self.nums[j])[i]) for j in range(len(self.nums))]
            for j in range(len(self.nums)):
                c[tmp_nums[j]] += 1

            for j in range(1, self.k+1):
                c[j] += c[j-1]

            for j in range(len(self.nums)-1, -1, -1):
                b[c[tmp_nums[j]]-1] = self.nums[j]
                c[tmp_nums[j]] -= 1

            self.nums = b