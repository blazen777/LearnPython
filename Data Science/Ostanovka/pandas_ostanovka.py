import pandas as pd

stations = pd.read_csv(
    open('ostanovka.csv', 'r', encoding='cp1251'),
    sep=';',
)

stations_count = stations.groupby('Street').size()
# for k, v in stations_count.items():
#     if v == stations_count.max():
#         print(k)
print(stations_count.idxmax())