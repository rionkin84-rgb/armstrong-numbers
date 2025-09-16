# armstrong_numbers.py

def is_armstrong(num: int) -> bool:
    """
    Проверка, является ли число Армстронга.
    """
    digits = str(num)
    n = len(digits)
    return num == sum(int(d)**n for d in digits)


def find_armstrong_numbers(n: int) -> list[int]:
    """
    Находит все n-значные числа Армстронга.
    n > 1 и n < 10
    """
    if n <= 1 or n >= 10:
        raise ValueError("n должно быть в диапазоне 2 <= n < 10")

    start = 10**(n - 1)
    end = 10**n
    return [num for num in range(start, end) if is_armstrong(num)]


if __name__ == "__main__":
    for n in range(2, 10):
        armstrongs = find_armstrong_numbers(n)
        if armstrongs:
            print(f"{n}-значные числа Армстронга: {armstrongs}")
