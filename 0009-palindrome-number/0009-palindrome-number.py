class Solution(object):
    def isPalindrome(self, x):
        r =0 
        num = x
        if x< 0:
            return False
        while(num !=0):
            r = r *10 + num % 10
            num = num //10
        return r == x


        