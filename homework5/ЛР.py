import pandas as pd
import numpy as np

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [20, 21, 22, 20, 23],
    "Department": ["Math", "Physics", "CS", "Math", "CS"],
    "GPA": [3.9, 3.5, 3.8, 3.7, 3.6],
    "Credits": [30, 28, 32, 30, 26]
}

data_fame = pd.DataFrame(data)


gpa = data_fame[data_fame["GPA"] > 3.7]
print(f'студенты с GPA > 3.7 {gpa}')
print()
math = data_fame[data_fame["Department"] == "Math"]
print(f'студенты математики {math}')
print()


sort_age = data_fame.sort_values(by="Age")
print(f'сортировка по возрасту {sort_age}')
print()
sort_gpa = data_fame.sort_values(by="GPA", ascending=False)
print(f'сортировка по GPA {sort_gpa}')
print()


avg_gpa = data_fame.groupby("Department")["GPA"].mean()
print(f'средний gpa {avg_gpa}')
print()
kolvo_students = data_fame["Department"].value_counts()
print(f'количество студентов {kolvo_students}')
print()


data_fame["Internship"] = [False, False, np.nan, True, np.nan]
propustili = data_fame[data_fame.isnull().any(axis=1)]
data_fame["Internship"].fillna(False, inplace=True)


data_fame["Final Credits"] = data_fame["Credits"] * data_fame["GPA"]
print(data_fame)
print()


data_sec_stud = data_fame.iloc[1]
print(f'данные о втором студенте {data_sec_stud}')
print()
three_stud = data_fame.iloc[:3, [0, 3]]
print(f'данные трех студентов {three_stud}')
print()
data_fame.iloc[3, 3] = 3.95


last_stolb = data_fame.iloc[:, -2:]
print(f'последние два столбца {last_stolb}')
print()
