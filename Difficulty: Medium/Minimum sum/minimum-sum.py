class Solution:
    def minSum(self, arr):
        arr.sort()
        num1, num2 = [], []
        for i, digit in enumerate(arr):
            if i % 2 == 0:
                num1.append(str(digit))
            else:
                num2.append(str(digit))
        
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            total = digit1 + digit2 + carry
            result.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1

        final_result = ''.join(result[::-1]).lstrip("0")
        return final_result if final_result else "0"




