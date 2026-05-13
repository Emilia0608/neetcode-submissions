# 리스트에 넣고 하나씩 더해주기
# nums 갯수만큼 반복, 더해지는 리스트에 새로운 숫자 없는 경우 추가
# 시간복잡도 O(n^3)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = [[num] for num in nums]

        for i in range(1, len(nums)):
            tmp_list = []
            for ans in answer:
                for num in nums:
                    if num not in ans:
                        new_ans = ans.copy()
                        new_ans.append(num)
                        tmp_list.append(new_ans)
            answer = tmp_list

        return answer


