import json
import random
import datetime

start_date = datetime.date(2020, 1, 1)
end_date = datetime.date(2020, 5, 18)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

python_data = []

for i in range(200):
  random_number_of_days = random.randrange(days_between_dates)
  random_date = start_date + datetime.timedelta(days=random_number_of_days)
  entry = {
      "model": "houseservices.houseservices",
      "pk": 100 + i,
      "fields": {
          "person": random.randint(20, 80),
          "breakfast": random.choice([True, False]),
          "lunch": random.choice([True, False]),
          "snack": random.choice([True, False]),
          "dinner": random.choice([True, False]),
          "shower": random.choice([True, False]),
          "sleep": random.choice([True, False]),
          "created_at": random_date,
          "updated_at": random_date
      }
  }
  python_data.append(entry)

with open('houseservices.json', 'w') as json_data:
  json.dump(python_data, json_data, default=str)
