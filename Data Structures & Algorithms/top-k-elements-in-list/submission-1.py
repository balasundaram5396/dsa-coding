class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for _ in range(len(nums)+1)]
        res=[]
        hmap={}
        for n in nums:
            hmap[n]=1+hmap.get(n,0)
        for key,v in hmap.items():
            freq[v].append(key)

        for i in range(len(freq)-1,-1,-1):
            for v in freq[i]:
                res.append(v)
                if len(res)==k:
                    return res
        return res