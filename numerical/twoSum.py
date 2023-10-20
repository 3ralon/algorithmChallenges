'''
Given an array of integers `nums` and an integer `target`, 
return indices of the two numbers that they add up to `target`.
'''

from typing import List, Any

class TwoSum():
    def twoSum(self, nums: List[int], target: int):
        for i,n in enumerate(nums):
            sub_nums = nums.copy()
            sub_nums.pop(i)
            if (addend := target - n) in sub_nums:
                return [i, nums.index(addend)]
        return []
                
        
    def test(self, nums: List[int], target: int, expected: List[Any]):
        try:
            result = self.twoSum(nums, target)
            assert(result == expected)
            print('✅ PASSED | Nums: {} | Target: {}'.format(nums,target))
        except:
            print('❌ FAILED | Nums: {} | Target: {}'.format(nums,target))
        print('- Expected: {}'.format(expected))
        print('- Result: {}'.format(result))
            
        
        
if __name__ == '__main__':
    ts = TwoSum()
    ts.test([1,2,3], 3, [0,1])
    ts.test([2,7,10,11], 21, [2,3])
    ts.test([1,2,3], 5, [1,2])
    ts.test([1,3,5,8,10], 8, [1,2])

    