# these are helper functions for the app

class NumberUtils:
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 0:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_perfect(n: int) -> bool:
        if n < 1:
            return False
        return sum(i for i in range(1, n) if n % i == 0) == n
    
    @staticmethod
    def is_armstrong(n: int) -> bool:
        num_string = str(abs(n))
        power = len(num_string)
        return sum(int(digit) ** power for digit in num_string) == abs(n)
    
    @staticmethod
    def classify_number(n: int) -> list:
        properties = []
        if NumberUtils.is_armstrong(n):
            properties.append("armstrong")
        properties.append("odd" if n % 2 != 0 else "even")
        return properties