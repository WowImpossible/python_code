# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#使用二分查找找到一个升序列表的target。

#创建的类
class Solution(object):
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            print(nums.index(target))
        except Exception as e:
            print("-1")

    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = len(nums)
        left = 0
        right = count - 1
        middle = 0
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right

        while left <= right:
            middle = (left + right)//2    #注意求整数是用//
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
        return -1


lst1 = [-1, 0, 3, 5, 9, 12]
#创建实例，真正干活的是类对象，而不是类
binary_search = Solution()
binary_search.search1(lst1, 9)
print(binary_search.search2(lst1, 9))
print(-9 % 4)



