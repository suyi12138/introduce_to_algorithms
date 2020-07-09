# 9.1

class MaxMin:

    def __init__(self, nums: list):
        # 待确认最大值和最小值的数组
        self.nums = nums

    def max_min(self):
        """
        :return:(max, min)
        """
        if not self.nums:
            return None

        length = len(self.nums)
        if length % 2 == 0 and length > 2:
            if self.nums[0] < self.nums[1]:
                min = self.nums[0]
                max = self.nums[1]
            else:
                min = self.nums[1]
                max = self.nums[0]
            for i in range(2, length-1, 2):
                if self.nums[i] < self.nums[i+1]:
                    if self.nums[i] < min:
                        min = self.nums[i]
                    if self.nums[i+1] > max:
                        max = self.nums[i+1]
                else:
                    if self.nums[i] > max:
                        max = self.nums[i]
                    if self.nums[i+1] < min:
                        min = self.nums[i+1]

        elif length == 2:
            if self.nums[0] < self.nums[1]:
                min = self.nums[0]
                max = self.nums[1]
            else:
                min = self.nums[1]
                max = self.nums[0]
        elif length == 1:
            min = max = self.nums[0]

        else:
            min = max = self.nums[0]
            for i in range(1, length-1, 2):
                if self.nums[i] < self.nums[i+1]:
                    if self.nums[i] < min:
                        min = self.nums[i]
                    if self.nums[i+1] > max:
                        max = self.nums[i+1]
                else:
                    if self.nums[i] > max:
                        max = self.nums[i]
                    if self.nums[i+1] < min:
                        min = self.nums[i+1]

        return (max, min)
