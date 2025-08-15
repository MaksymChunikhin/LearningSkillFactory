import random

def guess_number():
    number = random.randint(1, 100)  # загаданное число
    low = 1
    high = 100
    attempts = 0
    
    while True:
        guess = (low + high) // 2
        attempts += 1
        
        if guess == number:
            return attempts
        elif guess < number:
            low = guess + 1
        else:
            high = guess - 1

# Прогоняем много раз, чтобы узнать среднее количество попыток
trials = 1000
total_attempts = 0

for _ in range(trials):
    total_attempts += guess_number()

print(f"Среднее количество попыток за {trials} игр: {total_attempts / trials:.2f}")