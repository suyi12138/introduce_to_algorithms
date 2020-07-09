# 8.4

class BucketSort:

    def __init__(self, nums: list):
        # 待排序数组，假设数组中的数据均匀、独立地分布在[0, 1)区间上
        self.nums = nums

    def bucket_sort(self):
        length = len(self.nums)
        bucket = [[] for _ in range(length)]
        for i in range(length):
            bucket[int(length*self.nums[i])].append(self.nums[i])
        for i in range(length):
            for j in range(len(bucket[i])):
                for k in range(j+1):
                    if bucket[i][j] < bucket[i][k]:
                        bucket[i][j], bucket[i][k] = bucket[i][k], bucket[i][j]
                        break

        ans = []
        for i in range(length):
            for j in range(len(bucket[i])):
                ans.append(bucket[i][j])

        return ans