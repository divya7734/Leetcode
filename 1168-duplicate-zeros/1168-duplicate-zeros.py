class Solution(object):
    def duplicateZeros(self, arr):
        i=0
        n=len(arr)
        while i<n:
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i+=2
            else:
                i+=1