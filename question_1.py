# Task 1
import random

moods = ["Happy", "Sad", "Energetic", "Calm"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(len(days)):
    day = days[i]
    mood = random.choice(moods)
    print(f"{day} I feel {mood}")

