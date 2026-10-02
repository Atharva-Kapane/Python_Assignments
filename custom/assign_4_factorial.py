def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Enter a number >= 0")
    if num == 0:
        return 1

    fact = 1
    for i in range(2,num+1):
        fact *= i

    return fact


if __name__ == "__main__":
    print(factorial(5))
    print(factorial(10))