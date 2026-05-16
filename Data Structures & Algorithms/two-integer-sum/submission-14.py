# 하나씩 돌면서 더하면서 확인
# 두번째 숫자는 첫번째꺼 이후 인덱스부터 확인
# O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer_i, answer_j = 0, 0
        end_check = False

        for i in range(len(nums)):
            one = nums[i]
            for j in range(i+1, len(nums)):
                two = nums[j]
                if one + two == target:
                    end_check=True
                    answer_i=i
                    answer_j=j
                    break
                if end_check:
                    break
        
        return [answer_i, answer_j]
                    