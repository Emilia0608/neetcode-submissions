[6,9,10,1,2,3,4,5]
# for문을 다 돌면 안됨 -> O(n)이 됨
# 이분 탐색
## 첫 인덱스, 끝 인덱스, 중간 인덱스 값 비교
## 1. 첫 인덱스가 제일 작음 -> 첫 인덱스가 min값
## 2. 끝 인덱스가 제일 작음 -> 오른쪽 그룹 탐색
## 3. 중간 인덱스가 제일 작음
## -> 중간 인덱스 -1 값과 중간 인덱스 +1 값을 비교 -> 그룹 선택

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums) -> 이렇게 해도 정답이 되긴 함..;;

        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] <= nums[right]: # 그냥 바로 정답일 때 1 케이스
                return nums[left]

            mid = (left + right) // 2

            first = nums[left]
            middle = nums[mid]
            last = nums[right]

            # middle이 왼쪽 그룹에 있음
            if middle > last:
                left = mid + 1

            # middle이 오른쪽 그룹에 있음
            else:
                right = mid

        return nums[left]