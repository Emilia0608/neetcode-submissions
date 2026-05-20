[6,9,10,1,2,3,4,5]
# for문을 다 돌면 안됨 -> O(n)이 됨
# 이분 탐색
## 첫 인덱스, 끝 인덱스, 중간 인덱스 값 비교
## 1. 첫 인덱스가 제일 작음 -> 첫 인덱스가 min값
## 2. 끝 인덱스가 제일 작음 -> 오른쪽 그룹 탐색
## 3. 중간 인덱스가 제일 작음
## -> 3.1  

class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)