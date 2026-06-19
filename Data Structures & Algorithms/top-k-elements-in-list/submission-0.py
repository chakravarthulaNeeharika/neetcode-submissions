class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for x in nums:
            if x in count:
                count[x]+=1
            else:
                count[x]=1
        sorted_x=sorted(count.keys(),key=count.get,reverse=True)
        return sorted_x[:k]
            
            