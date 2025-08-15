import random

def guess_number(number):
    low, high = 1, 100
    attempts = 0
    while True:
        attempts += 1
        guess = (low + high) // 2
        if guess == number:
            return attempts
        elif guess < number:
            low = guess + 1
        else:
            high = guess - 1

random.seed(42)  # фиксируем генератор случайных чисел
attempts_list = [guess_number(random.randint(1, 100)) for _ in range(1000)]
print(f"Среднее количество попыток: {sum(attempts_list)/1000:.2f}")
