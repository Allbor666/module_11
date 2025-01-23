import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Использование библиотеки requests
# Запрашиваем данные с сайта
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    data = response.json()  # Получаем данные в формате JSON
    print("Полученные данные:")
    print(data[:3])  # Печатаем первые 3 записи для проверки

    # Преобразовываем данные в DataFrame
    df = pd.DataFrame(data)
    print("\nДанные в формате DataFrame:")
    print(df.head())
else:
    print(f"Ошибка при запросе: {response.status_code}")

# 2. Использование библиотеки pandas для анализа данных
print("\nСтатистическая информация:")
print(df.describe())  # Основные статистики по числовым столбцам

# Фильтруем посты, которые имеют ID больше 5
filtered_df = df[df['id'] > 5]
print("\nПосты с ID больше 5:")
print(filtered_df[['id', 'title']])

# 3. Использование библиотеки matplotlib для визуализации данных
# Визуализируем количество постов по ID
plt.figure(figsize=(10, 6))
plt.bar(df['id'], df['userId'], color='blue', alpha=0.7)
plt.xlabel("ID поста")
plt.ylabel("ID пользователя")
plt.title("Количество постов по ID пользователя")
plt.xticks(np.arange(1, 101, 5))  # Устанавливаем метки по оси X
plt.grid(True)

# Показываем график
plt.show()
