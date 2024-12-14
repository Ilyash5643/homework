import re
import matplotlib.pyplot as plt


file_name = "data_test.txt"

with open(file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()


tran = len(lines) - 1
print(f'Количество транзакций {tran}')


total = 0
for i in lines[1:]:
    helper = i.split(',')
    amount = float(helper[3].strip())
    total += amount
print(f'Общая сумма всех покупок {total}')


electro_tran = []
for i in lines[1:]:
    if re.search(r'Electronics', i):
        electro_tran.append(i.strip())
print('Транзакции с категорией Electronics')
for j in electro_tran:
    print(j)


price_tran = []
for i in lines[1:]:
    helper = i.split(',')
    amount = float(helper[3].strip())
    if amount > 100:
        price_tran.append(i.strip())
print('Транзакции с суммой больше 100 долларов')
for j in price_tran:
    print(j)


cat = {}
for i in lines[1:]:
    helper = i.split(',')
    category = helper[4].strip()
    if category in cat:
        cat[category] += 1
    else:
        cat[category] = 1

plt.figure(figsize=(10, 6))
plt.bar(cat.keys(), cat.values(), color='blue', edgecolor='black')
plt.title('Количество покупок в каждой категории', fontsize=12)
plt.xlabel('Категория', fontsize=12)
plt.ylabel('Количество покупок', fontsize=12)
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()

plt.savefig('category_histogram.png')
plt.show()
