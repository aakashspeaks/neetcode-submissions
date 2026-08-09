class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r=len(heights)-1
        max_area = 0

        while l<r:
            w= min(heights[l],heights[r])
            h = r-l
            max_area=max(max_area,w*h)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return max_area
        