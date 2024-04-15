import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta

# Генерация числовых данных
np.random.seed(0)
num_samples = 1000000

data = {
    'Age': np.random.randint(18, 65, num_samples),
    'Income': np.random.randint(20000, 100000, num_samples),
    'Experience_years': np.random.randint(0, 20, num_samples),
    'Score': np.random.uniform(1, 10, num_samples),
}

# Генерация категориальных данных
departments = ['IT', 'Finance', 'Marketing', 'HR']
data['Department'] = [random.choice(departments) for _ in range(num_samples)]

positions = ['Manager', 'Engineer', 'Analyst', 'Assistant']
data['Position'] = [random.choice(positions) for _ in range(num_samples)]

# Генерация данных о пользовательском поведении
activities = ['Reading', 'Gaming', 'Shopping', 'Socializing', 'Exercise']
data['Favorite_Activity'] = [random.choice(activities) for _ in range(num_samples)]
data['Daily_Screen_Time'] = np.random.randint(1, 12, num_samples)

# Генерация данных о предпочтениях
brands = ['Apple', 'Samsung', 'Google', 'Sony', 'Microsoft']
data['Preferred_Brand'] = [random.choice(brands) for _ in range(num_samples)]

# Генерация адресов электронной почты и номеров телефонов
def generate_email():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8)) + '@example.com'

def generate_phone():
    return '8' + ''.join(random.choice(string.digits) for i in range(10))

data['Email'] = [generate_email() for _ in range(num_samples)]
data['Phone'] = [generate_phone() for _ in range(num_samples)]

# Генерация данных о географическом положении и интересах
cities = ['Moscow', 'St. Petersburg', 'New York', 'London', 'Tokyo']
data['City'] = [random.choice(cities) for _ in range(num_samples)]

interests = ['Travel', 'Photography', 'Music', 'Cooking', 'Sports']
data['Interest'] = [random.choice(interests) for _ in range(num_samples)]

# Создание DataFrame
df = pd.DataFrame(data)

# Сохранение данных в CSV файл
df.to_csv('large_complex_statistical_data.csv', index=False)

print("Large complex dataset created and saved as 'large_complex_statistical_data.csv'")

