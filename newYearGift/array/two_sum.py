class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        common_nums = set(filter(lambda n: target - n in nums_set, nums_set))
        len_common_nums = len(common_nums)
        if len_common_nums == 3 :
            common_nums.discard(target/2)
            len_common_nums = 2
        
        if len_common_nums == 2 :
            n = common_nums.pop()
            m = common_nums.pop()
            return [nums.index(n), nums.index(m)]
        elif len_common_nums == 1 :
            n = common_nums.pop()
            i_n = nums.index(n)
            i_m = nums[i_n+1:].index(n) + i_n + 1
            return [i_n, i_m]
