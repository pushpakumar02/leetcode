class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = int(num1), int(num2)

        num3 = num1 * num2
        return str(num3)