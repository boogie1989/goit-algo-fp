import random
import matplotlib.pyplot as plt

# Кількість кидків кубиків
num_rolls = 1000000

# Словник для підрахунку сум
sum_counts = {sum_value: 0 for sum_value in range(2, 13)}

# Симуляція кидків
for _ in range(num_rolls):
    roll_sum = random.randint(1, 6) + random.randint(1, 6)
    sum_counts[roll_sum] += 1

# Обчислення ймовірностей
probabilities = {sum_value: count /
                 num_rolls for sum_value, count in sum_counts.items()}

# Вивід результатів
print("Сума\tІмовірність")
for sum_value, probability in probabilities.items():
    print(f"{sum_value}\t{probability:.2%}")

# Графік імовірностей
plt.bar(probabilities.keys(), probabilities.values())
plt.xlabel('Сума кубиків')
plt.ylabel('Імовірність')
plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
plt.xticks(range(2, 13))
plt.show()
