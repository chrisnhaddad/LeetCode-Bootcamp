class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0
        i = 0

        if not s:
            return result

        while (i < len(s) and (s[i] == " ")):
            i+=1

        if i == len(s):
            return result


        sign = 1
        if (s[i] == '-'):
            sign = -1
            i+=1
        elif (s[i] == '+'):
            i+=1

        while ((i < len(s)) and (s[i].isdigit())):
            result = result * 10 + int(s[i])
            i+=1
        
        result *= sign

        if (result < -2**31):
            result = -2**31
        elif (result > (2**31 - 1)):
            result = 2**31 - 1

        return result