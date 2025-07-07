from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        feq = Counter(s)
        str = sorted(feq.items() , key = lambda x:  (-x[1],x[0]))
        return "".join (char* count for char , count in str)


        