# 투포인터로 젤 끝 두 개의 값이 target보다 크면 뒷 포인터를 하나씩 땡겨오기
# 작으면 앞 포인터를 올리기
# target과 같으면 끝
# 아마도 1-indexed 라는게 1부터 인덱스를 세라 뭐 그런거인듯

# 시간 복잡도 O(n)
# additional space? => 입력 배열 말고 새로 얼마나 메모리를 더 쓰냐
# 현재 코드에서는 start 변수랑 end 만 씀 -> O(1)임

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1
        while numbers[start] + numbers[end] != target:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
        return [start+1, end+1]

        
