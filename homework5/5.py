import pandas as pd


data = {
    'Stolb': [100, 150, 200, 250, 300]
}

DataFrame = pd.DataFrame(data)
DataFrame['Nakopit'] = DataFrame['Stolb'].cumsum()
print(DataFrame)
