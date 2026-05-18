# 0 아니면 정답에 append
# 0의 갯수 카운트
# nums 다 돌고 0 갯수 카운트 된 만큼 0 append
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for idx, num in enumerate(nums):
            if num == 0:
                count += 1
        for i in range(count):
            nums.remove(0)
        for i in range(count):
            nums.append(0)

        