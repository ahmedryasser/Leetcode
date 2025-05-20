class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        ans = []
        for cnt, upg, sl, m in zip(count,upgrade,sell,money):
            total = cnt*sl + m 
            ans.append(min(cnt,total//(sl+upg))) 
        return ans
            

