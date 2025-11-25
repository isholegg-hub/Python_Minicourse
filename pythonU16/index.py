# Як швидко очистити дані від сміття а Pandas?


import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Olya", "Ivan", "", None, "Marta"],
    "score": [95, None, 88, 70, None],
    "class": [None, "10A", "", "11B", None]
})

# Замінюємо пусті рядки на NaN
df.replace("", np.nan, inplace=True)

# Тепер заповнюємо пропуски
clean_fill = df.fillna({
    "name": "Unknown",
    "score": df["score"].mean(),
    "class": "Not assigned"
})

print(clean_fill)
