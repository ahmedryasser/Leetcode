class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq_arr = {}
        freq_target = {}
        for item,tar in zip(arr,target):
            freq_arr[item] = freq_arr.get(item, 0)+1
            freq_target[tar] = freq_target.get(tar, 0)+1
        
        return freq_target == freq_arr
        