# Armstrong Numbers Finder

## Условие задачи
**9.** Число, состоящее из `n` ( `n > 1` ) цифр, называется **числом Армстронга**, если сумма его цифр, возведённых в `n`-ю степень, равна самому этому числу.  

Например:  
- `153 = 1³ + 5³ + 3³`  
- `1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴`  

Составить программу, которая будет находить все `n`-значные числа Армстронга (`n < 10`).  

---

## Программа
Код реализован на Python:

```python
def is_armstrong(num: int) -> bool:
    digits = str(num)
    n = len(digits)
    return num == sum(int(d)**n for d in digits)


def find_armstrong_numbers(n: int) -> list[int]:
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







Как запустить

Клонировать репозиторий:

git clone https://github.com/rionkin84-rgb/armstrong-numbers.git
cd armstrong-numbers


Запустить программу:

python armstrong_numbers.py

Пример вывода
3-значные числа Армстронга: [153, 370, 371, 407]
4-значные числа Армстронга: [1634, 8208, 9474]
5-значные числа Армстронга: [54748, 92727, 93084]
6-значные числа Армстронга: [548834]
7-значные числа Армстронга: [1741725, 4210818, 9800817, 9926315]
8-значные числа Армстронга: [24678050, 24678051, 88593477]
9-значные числа Армстронга: [146511208, 472335975, 534494836, 912985153]


✍️ Авторы: rionkin84-rgb(Ионкин Р.В), 3oza(Загарских А.А)