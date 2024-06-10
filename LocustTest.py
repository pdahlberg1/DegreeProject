from datetime import datetime
from locust import HttpUser, task, between
import random
import json

TOKEN = "YOUR TOKEN HERE"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

class FastAPIUser(HttpUser):
    wait_time = between(1, 5) # Time between requests is 1-5 second

    @task(1)  # GET task
    def get_events(self):
        user_id = random.randint(1, 4)
        self.client.get(f"/read/query_events/{user_id}", headers=headers)

    @task(10)  # POST task (10 times more frequent), with random example data
    def write_daily_record(self):
        item = {
            "timestamp": datetime.now().isoformat(),
            "headache_intensity": random.randint(0, 4),
            "headache_start": datetime.now().isoformat(),
            "mood_level": random.randint(0, 4),
            "exercise_duration": random.randint(0, 120),
            "exercise_intensity": random.randint(0, 4),
            "had_breakfast": random.randint(0, 1),
            "had_lunch": random.randint(0, 1),
            "had_dinner": random.randint(0, 1),
            "heart_rate": random.randint(60, 120),
            "stress_level": random.randint(0, 4)
        }
        self.client.post("/write/daily_record", data=json.dumps(item), headers=headers)
