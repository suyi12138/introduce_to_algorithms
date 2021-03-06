# 4.1 最大子数组


class FindMaximumSubarray:

    def __init__(self, nums: list):
        self.nums = nums

    def find_max_crossing_subarray(self, low: int, mid: int, high: int):
        left_sum = float('-inf')
        sum = 0
        for i in range(mid, low-1, -1):
            sum = sum + self.nums[i]
            if sum > left_sum:
                left_sum = sum
                max_left = i

        right_sum = float('-inf')
        sum = 0
        for i in range(mid+1, high+1):
            sum = sum + self.nums[i]
            if sum > right_sum:
                right_sum = sum
                max_right = i

        return (max_left, max_right, left_sum + right_sum)

    def find_max_subarray(self, low: int, high: int):
        if high == low:
            return (low, high, self.nums[low])

        else:
            mid = (low + high) // 2
            (left_low, left_high, left_sum) = self.find_max_subarray(low, mid)
            (right_low, right_high, right_sum) = self.find_max_subarray(mid+1, high)
            (cross_low, cross_high, cross_sum) = self.find_max_crossing_subarray(low, mid, high)

            if left_sum >= right_sum and left_sum >= cross_sum:
                return (left_low, left_high, left_sum)
            elif right_sum >= left_sum and right_sum >= cross_sum:
                return (right_low, right_high, right_sum)
            else:
                return (cross_low, cross_high, cross_sum)