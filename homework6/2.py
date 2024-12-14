import re
import matplotlib.pyplot as plt

file_path = 'data.txt'

dates = []
temperatures = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # извлечение даты и температуры
        match = re.search(r'(\d{4}-\d{2}-\d{2}): Temperature = (\d+)°C', line)
        if match:
            dates.append(match.group(1))  # Первая группа — дата
            temperatures.append(int(match.group(2)))  # Вторая группа — температура


plt.figure(figsize=(5, 5))
plt.hist(temperatures, bins=range(min(temperatures), max(temperatures) + 1), edgecolor='black', alpha=0.5)
plt.title('Гистограмма температуры', fontsize=12)
plt.xlabel('Температура', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
