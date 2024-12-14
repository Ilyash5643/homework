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


max_temperature = max(temperatures)
max_temperature1 = temperatures.index(max_temperature)
date_m_t = dates[max_temperature1]
print(date_m_t)

plt.figure(figsize=(10, 6))
plt.plot(dates, temperatures, marker='o', linestyle='-', color='b', label='Temperature')
plt.title('Температура по дням', fontsize=16)
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Температура (°C)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('temperature_plot.png')
plt.show()
