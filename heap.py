# 6.1 - 6.4

class Heap:

    def __init__(self, nums: list):
        self.nums = nums
        self.nums_length = len(nums)
        self.heap_length = len(nums)

    def left(self, node: int):
        """
        :param node: the subscript of the current node in the array 'nums'
        :return: the subscript of the left child node
        """
        return 2 * (node + 1) - 1

    def right(self, node: int):
        """
        :param node: the subscript of the current node in the array 'nums'
        :return: the subscript of the right child node
        """
        return 2 * (node + 1)

    def parent(self, node: int):
        """
        :param node: the subscript of the current node in the array 'nums'
        :return: the subscript of the parent node
        """
        return (node + 1) // 2 - 1

    def max_heapify(self, root: int):
        """
        Construct the subtree with the root node whose subscript is 'root' into the maximum heap
        :param root: the subscript of the root node
        """
        l = self.left(root)
        r = self.right(root)
        if l < self.heap_length and self.nums[l] > self.nums[root]:
            largest = l
        else:
            largest = root
        if r < self.heap_length and self.nums[r] > self.nums[largest]:
            largest = r
        if largest != root:
            self.nums[root], self.nums[largest] = self.nums[largest], self.nums[root]
            self.max_heapify(largest)

    def build_max_heap(self):
        self.heap_length = self.nums_length
        for i in range(self.heap_length//2-1, -1, -1):
            self.max_heapify(i)

    def heapsort(self):
        self.build_max_heap()
        for i in range(self.nums_length-1, 0, -1):
            self.nums[0], self.nums[i] = self.nums[i], self.nums[0]
            self.heap_length -= 1
            self.max_heapify(0)



