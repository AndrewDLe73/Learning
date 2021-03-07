'''
315. Count of Smaller Numbers After Self
Hard
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
'''


'''
Forced Method
'''


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        answer = []
        while len(answer) < len(nums):
            count = 0
            for index in range(0, len(nums)):
                current = nums[index]
                next = index + 1
                if index == len(nums)-1:
                    answer.append(0)
                    continue
                test = nums[next:]
                while len(test) > 0:
                    compare = test[0]
                    if compare < current:
                        count += 1
                    test.pop(0)
                answer.append(count)
                count = 0
        return answer


'''
Working Backwards
'''
h
